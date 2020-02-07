import sys
sys.path.append('..')
from Utilities.Constants import TradeSignal


class IStrategy(object):

    def __init__(self, strategy_name: str):
        self.name = strategy_name

    @staticmethod
    def get_trade_signal(self, **kwargs) -> TradeSignal:
        pass
