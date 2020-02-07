import sys
sys.path.append('..')
from Structures.Asset import Asset
from Interfaces.IStrategy import IStrategy


class ExecutionUnit(object):

    def __init__(self, asset: Asset, update_interval: int, strategy: IStrategy):
        self.asset = asset
        self.strategy = strategy
        self.update_interval = update_interval
