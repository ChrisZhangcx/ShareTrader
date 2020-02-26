from enum import IntEnum


class TradeSignal(IntEnum):
    hold = 0
    buy = 1
    sell = 2


class AssetType(IntEnum):
    Stock = 0
    Futures = 1
    Fund = 2
