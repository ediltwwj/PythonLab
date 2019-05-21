import time
import datetime

"""实验四第二题"""


def bin_valid_date(date):
    """输入日期判断格式是否合法，合法输出季节"""

    month = ["", "冬季", "冬季", "春季", "春季", "春季", "夏季", "夏季", "夏季", "秋季", "秋季", "秋季", "冬季"]
    try:
        time.strptime(date, "%Y-%m-%d")
        validData = time.strptime(date, "%Y-%m-%d")
        print("日期合法，是{}".format(month[validData.tm_mon]))
    except:
        print("日期不合法")


if __name__ == "__main__":
    date = input("请输入日期(年-月-日)：")
    bin_valid_date(date)