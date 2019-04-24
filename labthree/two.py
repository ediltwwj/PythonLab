"""实验三第二题"""


def cerate_card(num, cardId, defaultPwd):
    """随机生成n个卡号，默认初始密码"""

    dict = {}
    length = len(str(num))

    for i in range(1, num + 1):
        dict[cardId + str(i).rjust(length, '0')] = defaultPwd

    print("账号          密码")

    for key, value in dict.items():
        print(key + " " + value)


if __name__ == "__main__":
    num = 100
    cardId = "6102009"
    defaultPwd = "redhat"

    cerate_card(num, cardId, defaultPwd)
