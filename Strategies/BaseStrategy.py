from Utilities.Constants import AssetType, TradeSignal


class BaseStrategy(object):
    def __init__(self, name: str):
        """
        :param name: 策略的名称
        """
        self.name = name
        self.signal = None      # （上一次获得的）交易信号

    def get_trade_signal(self, asset_type: AssetType, ts_code: str, **kwargs):
        if asset_type == AssetType.Futures:
            self.signal = self._get_future_signal(ts_code, **kwargs)
        elif asset_type == AssetType.Stock:
            self.signal = self._get_stock_signal(ts_code, **kwargs)
        elif asset_type == AssetType.Fund:
            self.signal = self._get_fund_signal(ts_code, **kwargs)
        else:
            raise AttributeError("不支持的资产类型")

    def _get_future_signal(self, ts_code: str, **kwargs) -> TradeSignal:
        raise NotImplementedError("策略 {} 尚未实现对 期权 类型资产的监控机制")

    def _get_stock_signal(self, ts_code: str, **kwargs) -> TradeSignal:
        raise NotImplementedError("策略 {} 尚未实现对 股票 类型资产的监控机制")

    def _get_fund_signal(self, ts_code: str, **kwargs) -> TradeSignal:
        raise NotImplementedError("策略 {} 尚未实现对 基金 类型资产的监控机制")

    def __repr__(self):
        return "当前使用的策略名称：{}\n".format(self.name)
