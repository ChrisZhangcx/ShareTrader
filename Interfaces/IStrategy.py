from abc import abstractmethod, ABCMeta

import sys
sys.path.append('..')
from Structures.Constants import TradeSignal


class IStrategy(object, metaclass=ABCMeta):

    def __init__(self, strategy_name: str):
        self.name = strategy_name

    @abstractmethod
    def get_trade_signal(self, **kwargs) -> TradeSignal:
        pass

    def __repr__(self):
        return "当前使用的策略：{}".format(self.name)
