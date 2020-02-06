# 该文件用于开发时的测试
import tushare as ts

import sys
sys.path.append('..')
from Structures.FundRequestor import FundRequestor
from Utilities.file_utils import json_reader


def main():
    hold_config_path = r"../hold_config.json"
    hold_config = json_reader(hold_config_path)

    fund_codes = hold_config['fund']['fund_code']

    pro = ts.pro_api()
    fund_requestor = FundRequestor(pro)
    for code in fund_codes:
        daily = fund_requestor.get_fund_value_daily(code)
    return


if __name__ == '__main__':
    main()
