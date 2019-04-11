# 7-13

def findStringPosition():
    """查找字符串或者字符第一次出现的位置"""

    mainStr = input()  # 主串
    subStr = input()  # 子串

    subStrPos = mainStr.find(subStr)  # 子串在主串的位置

    if subStrPos < 0:
        print("can't find letter {}".format(subStr))
    else:
        print("index={}".format(subStrPos + 1))


if __name__ == "__main__":

    findStringPosition()
