import os
import pickle

import sys
sys.path.append('..')
from Strategies.MacdStrategy import MacdStrategy
from Utilities.Constants import AssetType
from Structures.ExecutionUnit import ExecutionUnit, Asset


# 根据传入的指定策略名称，返回给定的策略
def choose_strategy(strategy_name: str):
    if strategy_name == "macd":
        return MacdStrategy()
    else:
        raise NotImplementedError("所选策略尚未实现！")


def choose_asset_type(asset_type: int) -> AssetType:
    if asset_type == 1:
        return AssetType.Share
    elif asset_type == 2:
        return AssetType.Futures
    elif asset_type == 3:
        return AssetType.Fund
    else:
        raise AttributeError("输入的资产类型有误，请检查。")


# 检查对应代码的资产是否已经在本地，对于没有保存的资产配置，生成ExecutionUnit，并保存到本地
def get_asset_unit(ts_code: str) -> ExecutionUnit:
    file_path = os.path.join("../AssetLogger", ts_code + ".cfg")
    if os.path.exists(file_path):
        return pickle.load(open(file_path, "rb"))
    else:
        exe_unit = init_unit(ts_code)
        pickle.dump(exe_unit, open(file_path, "wb"))
        return exe_unit


# 初始化一个ExecutionUnit
def init_unit(ts_code: str) -> ExecutionUnit:
    while True:
        print("----- 尚未保存给定资产的监控配置，进入初始化模式 -----")
        print("初始化资产代码：{}".format(ts_code))
        # 资产信息
        ts_type = input("请输入当前资产的所属类型，其中：1-股票，2-期货，3-基金。\n\t输入：")
        if ts_type not in ["1", "2", "3"]:
            print("输入格式有误，请重试")
            continue
        ts_type = choose_asset_type(int(ts_type))
        ts_name = input("请输入当前资产的名称：")
        ts_remark = input("请输入当前资产的备注，如果不输入，可直接键入回车：")
        # 策略信息
        strategy = input("请选择要对该资产使用的监控策略，此处将默认你已知晓所有可选策略名称：")
        strategy = choose_strategy(strategy)
        # 更新间隔
        interval = input("请输入定期执行该策略的时间间隔（分钟）：")
        try: interval = int(interval)
        except: continue
        break
    cur_asset = Asset(ts_code, ts_name, ts_type, ts_remark)
    cur_unit = ExecutionUnit(asset=cur_asset, update_interval=interval, strategy=strategy)
    return cur_unit
