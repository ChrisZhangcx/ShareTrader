import sys
sys.path.append('..')
from Interfaces.IStrategy import IStrategy


def choose_strategy(strategy_name: str) -> IStrategy:
    if strategy_name == "turtle":
        return