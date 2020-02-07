import sys
sys.path.append('..')
from Interfaces.IStrategy import IStrategy
from Utilities.Constants import TradeSignal


class TestStrategy(IStrategy):
    # 一个用来测试的策略。无论传入什么参数，都返回“继续持有”信号
    def __init__(self):
        super(TestStrategy, self).__init__("test strategy")

    @staticmethod
    def get_trade_signal(**kwargs) -> TradeSignal:
        # 应当根据具体情况来返回不同的信号，且该函数中不进行输出
        print("Test Strategy接收到一次返回信号请求。")
        print("传入数据为：")
        print(kwargs)
        return TradeSignal.hold

    def __repr__(self):
        return "----- 使用策略：{} -----".format("Test Strategy")
