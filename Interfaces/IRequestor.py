# 用于请求数据的接口
from abc import abstractclassmethod, ABCMeta


class IRequestor(object, metaclass=ABCMeta):
    def __init__(self, pro, name: str):
        # pro: tushare的api接口
        # name: 当前请求工具的名称
        self._name = name
        self._pro = pro

    def get_name(self) -> str:
        return self._name

    def get_pro(self):
        return self._pro


if __name__ == '__main__':
    pass
