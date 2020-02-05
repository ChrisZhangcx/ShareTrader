# 初始化文件：根据传入的用户token来进行API调用
#   用户token在TuShare中被用于标识用户的权限，不同权限的账户能获得的信息量不同
#   请确保账户拥有未来操作所需要的权限
import argparse

import tushare as ts


parser = argparse.ArgumentParser()
parser.add_argument(
    "-t", "--token",
    help="为调用TuShare行情获取接口，请输入你在该网站的用户token。"
)
args = parser.parse_args()


def main():
    if args.token is None:
        raise AttributeError("请在调用该初始化文件时传入用户token。")

    print("----- 检测到传入的用户token，开始设置私人接口... -----")
    print("  * 请确认token无误，否则可能无法成功返回历史数据，")
    print("  * 如果需要重置token，重新运行当前文件即可。")
    ts.set_token(args.token)
    print("设置用户token成功！")


if __name__ == '__main__':
    main()
