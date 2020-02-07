import sys
sys.path.append('..')
from Structures.Asset import Asset
from Interfaces.IStrategy import IStrategy


class ExecutionUnit(object):

    def __init__(self, asset: Asset, update_interval: int, strategy: IStrategy):
        self.asset = asset
        self.strategy = strategy
        self.update_interval = update_interval

    def __repr__(self):
        return "---------- 执行单元信息 ----------\n" + \
               self.asset.__repr__() + \
               "\n" + self.strategy.__repr__(self.strategy) + \
               "\n----- 更新间隔：{} 分钟 -----".format(self.update_interval)
