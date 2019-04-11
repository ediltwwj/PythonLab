"""实验二"""


def hierarchy():
    """成绩等级划分"""

    score = float(input("Please input the score(0 -100) : "))

    assert score >= 0.0 and score <= 100.0, \
        "value must be valid!"

    if score >= 90.0:
        print("A")
    elif score >= 80.0:
        print("B")
    elif score >= 70.0:
        print("C")
    elif score >= 60.0:
        print("D")
    else:
        print("E")


def primeSum():
    """计算100-1000以内所有素数之和"""

    flag = True
    sum = 0

    for i in range(100, 1001):
        for j in range(2, i):
            if (i % j == 0):
                flag = False
        if flag:
            sum += i
        flag = True

    print("Sum = {}".format(sum))


def printMultTable():
    """打印下三角的九九乘方表"""

    for i in range(1, 10):
        for j in range(1, 10):
            if j <= i:
                print("{} * {} = {:2d}".format(j, i, i * j), end=' ')
        print()


if __name__ == "__main__":
    hierarchy()  # 成绩等级划分
    print()
    primeSum()  # 打印100-1000范围的素数和
    print()
    printMultTable()  # 打印下三角九九乘方表
