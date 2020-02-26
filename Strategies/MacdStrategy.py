import talib
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append('..')
from Strategies.BaseStrategy import BaseStrategy
from Utilities.Constants import TradeSignal, AssetType


class MacdStrategy(BaseStrategy):
    def __init__(self, name: str = "MACD", fast_period: int = 12, slow_period: int = 26):
        """
        :param name: 策略名称，默认为MACD
        :param fast_period: 快线周期
        :param slow_period: 慢线周期
        """
        super(MacdStrategy, self).__init__(name=name)
        self.fast_period = fast_period
        self.slow_period = slow_period

    def _get_fund_signal(self, ts_code: str, **kwargs) -> TradeSignal:
        # 获取收盘价数据
        pro = ts.pro_api()
        stock_daily = pro.daily(ts_code=ts_code)
        close_price = stock_daily['close']

        macd = pd.DataFrame()
        a, b, c = talib.MACD(close_price)
        macd['macdhist'] = c
        macd.plot()
        plt.show()
        # macd计算：快线（12天）-慢线（26天）
        # 应当根据具体情况来返回不同的信号，且该函数中不进行输出
        return TradeSignal.hold

    def set_periods(self, fast_period: int = None, slow_period: int = None):
        if fast_period is None and slow_period is None:
            print("----- 设置策略失败：没有传入任何信息 -----")
            return
        self.fast_period = fast_period
        self.slow_period = slow_period
