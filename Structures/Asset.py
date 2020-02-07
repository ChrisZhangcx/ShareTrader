# 资产的基本单元，保存资产通用的基本信息，如：TS代码，资产名称，额外信息等
import sys
sys.path.append('..')
from Structures.Constants import AssetType


class Asset(object):
    def __init__(self, ts_code: str, name: str, asset_type: AssetType, remark: str = None):
        self.ts_code = ts_code
        self.name = name
        self.type = asset_type
        self.remark = remark

    def __repr__(self):
        return "----- 资产信息 -----\n" + \
               "资产名称：{}；所属类型：{}".format(self.name, self.type) + \
               ("。备注：{}".format(self.remark) if self.remark is not None else "")
