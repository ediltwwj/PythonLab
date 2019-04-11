# 7-1

def printMultTable():
    """打印九九乘法表，结果占4个宽度"""

    for firstMult in range(1, 10):
        for secondMult in range(1, 10):
            print("{}*{}={:<4}".format(firstMult, secondMult, firstMult * secondMult), end='')

        print()


if __name__ == "__main__":
    printMultTable()
