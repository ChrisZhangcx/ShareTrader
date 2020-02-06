import pandas as pd

import sys
sys.path.append('..')
from Interfaces.IRequestor import IRequestor


class FundRequestor(IRequestor):
    def __init__(self, pro, name: str = "FundRequestor"):
        super(FundRequestor, self).__init__(pro=pro, name=name)

    # 获得场内/场外所有基金的信息
    def get_all_fund(self, market: str ='O') -> pd.DataFrame:
        # market: 场内-E, 场外-O
        return self._pro.fund_basic(market=market)

    # 通过基金代码，获得基金的净值信息
    def get_fund_value_daily(self, fund_code: str):
        # fund_code: 基金代码，如：165509.SZ
        return self._pro.fund_nav(ts_code=fund_code)

    # 通过基金代码，获得基金的持仓信息
    def get_fund_portfolio(self, fund_code: str):
        # fund_code: 基金代码，如：165509.SZ
        return self._pro.fund_portfolio(ts_code=fund_code)
