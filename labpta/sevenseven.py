# 7-7

def calcuDepositInterest(money, year, rate):
    """根据money(存款金额),year(存期),rate(年利率)来计算税前存款利息"""

    assert money > 0. and year > 0. and rate > 0., \
        "Value must be valid"

    interest = money * (1.0 + rate) ** year - money

    print("interest={:.2f}".format(interest))


if __name__ == "__main__":

    money, year, rate = map(float, input().split())
    calcuDepositInterest(money, year, rate)
