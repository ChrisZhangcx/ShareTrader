import sys
sys.path.append('..')
from Interfaces.IStrategy import IStrategy
from Structures.Constants import TradeSignal


class TestStrategy(IStrategy):
    # 一个用来测试的策略。无论传入什么参数，都返回“继续持有”信号
    def __init__(self):
        super(TestStrategy, self).__init__("test strategy")

    def get_trade_signal(self, **kwargs) -> TradeSignal:
        return TradeSignal.hold

    def __repr__(self):
        return "----- 使用策略：{} -----".format("Test Strategy")
