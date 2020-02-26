import sys
sys.path.append('..')
from Structures.Asset import Asset
from Strategies.BaseStrategy import BaseStrategy


class ExecutionUnit(object):

    def __init__(self, asset: Asset, strategy: BaseStrategy, update_interval: int):
        self.asset = asset
        self.strategy = strategy
        self.update_interval = update_interval

    def __repr__(self):
        return "---------- 执行单元信息 ----------\n" + \
               self.asset.__repr__() + \
               "\n" + self.strategy.__repr__() + \
               "\n----- 更新间隔：{} 分钟 -----".format(self.update_interval)
