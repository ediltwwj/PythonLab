"""实验四第一题"""

if __name__ == "__main__":
    str = "1234567890"

    print("截取字符串第一位到第三位的字符 : {}".format(str[0: 3]))
    print("截取字符串最后三位的字符 : {}".format(str[-3:]))
    print("截取字符串的全部字符 : {}".format(str[:]))
    print("截取字符串的第七个字符到结尾 : {}".format(str[6:]))
    print("截取字符串第一位到倒数第三位之间的字符 : {}".format(str[: -3]))
    print("截取字符串的第三个字符 : {}".format(str[2: 3]))
    print("截取字符串的最后一个字符 : {}".format(str[-1:]))
    print("截取与原字符串顺序相反的字符串 : {}".format(str[:: -1]))
