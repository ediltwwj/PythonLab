import random
from math import pi

"""实验一"""


class Calculator:
    """实现计算器功能"""

    def normalFunc(self):
        """普通计算"""

        x, y = map(int, input("input two integer x and y : ").split(' '))
        print("x + y = {}".format(x + y))
        print("x - y = {}".format(x - y))
        print("x * y = {}".format(x * y))
        print("x / y = {}".format(x / y))
        print("x // y = {}".format(x // y))

    def complexFunc(self):
        """复数计算"""

        c1 = eval(input("c1 = "))
        c2 = eval(input("c2 = "))
        print("c1 + c2 = {}".format(c1 + c2))
        print("c1 - c2 = {}".format(c1 - c2))


class Cylinder:
    """计算圆柱体体积和表面积"""

    def __init__(self, r, h):
        self._r = r
        self._h = h

    def getArea(self):
        """计算圆柱体表面体"""
        return 2.0 * pi * (self._r ** 2.0 + self._h)

    def getVolumn(self):
        """计算圆柱体体积"""
        return pi * self._r ** 2.0 * self._h


def printRandom():
    """实现随机数的格式化输出"""

    for i in range(50):
        x = random.randint(0, 10000)
        print("%04d" % (x), end=' ')
        if (i + 1) % 5 == 0:
            print(' ')


if __name__ == "__main__":
    # Cylinder类测试
    print("\nCylinder类测试!!!")
    cyli = Cylinder(2.0, 2.0)
    print("Area : {:-10.3f}".format(cyli.getArea()))
    print("Volumn : {:-10.3f}".format(cyli.getVolumn()))

    # Calculator类测试
    print("\nCalculator类测试!!!")
    cala = Calculator()
    cala.normalFunc()
    cala.complexFunc()

    # printRandom()方法测试
    print("\nprintRandom()方法测试!!!")
    printRandom()
