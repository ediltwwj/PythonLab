# 7-5

import math


def printCircleArea(radius):
    """根据半径求圆的面积,并输出"""

    area = math.pi * radius ** 2
    print("{:.2f}".format(area))


if __name__ == "__main__":

    radius = float(input())
    printCircleArea(radius)
