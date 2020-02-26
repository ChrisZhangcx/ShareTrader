import datetime
import talib
import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append('..')
from Strategies.BaseStrategy import BaseStrategy
from Utilities.Constants import TradeSignal, AssetType


class MacdStrategy(BaseStrategy):
    def __init__(self, name: str = "MACD", fast_period: int = 12, slow_period: int = 26, signal_period: int = 9):
        """
        :param name: 策略名称，默认为MACD
        :param fast_period: 快线周期
        :param slow_period: 慢线周期
        """
        super(MacdStrategy, self).__init__(name=name)
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period

    def _get_stock_signal(self, ts_code: str, **kwargs) -> TradeSignal:
        # 获得今日日期
        current_date = datetime.datetime.now()
        current_day = "{}{}{}".format(current_date.year, current_date.month, current_date.day)
        # 获得指定股票的收盘价数据
        pro = ts.pro_api()
        stock_daily = pro.daily(ts_code=ts_code, start_date="20191201")
        stock_day = stock_daily['trade_date'][0]
        if current_day != stock_day:
            print("* 注意：今日收盘价尚未公布，返回的信息使用的数据截止到昨日收盘价。")
        # 计算MACD值
        # 由于在返回的数据中距离当前日期越近的index越小，因此计算均值时需要传入逆序数据
        macd, signal, hist = self.__get_macd_result(np.array(stock_daily['close'])[::-1])
        signal_refer = hist[-1]
        # TODO: 根据返回的MACD信号返回交易信号：量化？
        return TradeSignal.hold

    def __get_macd_result(self, close_price: np.ndarray):
        macd, signal, hist = talib.MACD(close_price, fastperiod=self.fast_period, slowperiod=self.slow_period,
                                        signalperiod=self.signal_period)
        return macd, signal, hist

    def set_periods(self, fast_period: int = None, slow_period: int = None, signal_period: int = None):
        if fast_period is None and slow_period is None and signal_period is None:
            print("----- 设置策略失败：没有传入任何信息 -----")
            return
        if fast_period is not None:
            self.fast_period = fast_period
        if slow_period is not None:
            self.slow_period = slow_period
        if signal_period is not None:
            self.signal_period = signal_period

    def get_periods(self):
        print("正在查看的MACD参数为：快线周期{}，慢线周期{}，信号周期{}".format(
            self.fast_period, self.slow_period, self.signal_period
        ))


# 测试MACD接口的使用
if __name__ == '__main__':
    import numpy as np

    pro = ts.pro_api()
    df = pro.daily(ts_code="000001.SZ", start_date="20150401", end_date="20151110")
    d = np.array(df['close'][:34])
    macd = list()
    signal = list()
    for idx in range(25, 34):
        a = d[idx-11:idx + 1]
        macd.append(np.mean(a))
        b = d[idx-25:idx + 1]
        signal.append(np.mean(b))
    c = [macd[i] - signal[i] for i in range(9)]
    hist = np.mean(c)
    # talib 的macd
    macd1, signal1, hist1 = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)

    fig = plt.figure(figsize=[18, 5])
    plt.plot(df.index, macd1, label="macd")
    plt.plot(df.index, signal1, label="signal")
    plt.plot(df.index, hist1, label="hist")
    plt.legend(loc="best")
    plt.show()
    print()
