"""实验三第二题"""


def printMultTable():
    """打印下三角的九九乘方表"""

    for i in range(1, 10):
        for j in range(1, 10):
            if j <= i:
                print("{} * {} = {:2d}".format(j, i, i * j), end=' ')
        print()


if __name__ == "__main__":
    printMultTable()
