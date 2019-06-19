"""实验八第二题"""


class Vector:

    def __init__(self, a=0, b=0, c=0):
        """构造方法"""

        self.__a = a
        self.__b = b
        self.__c = c

    def get_vec_a(self):
        """返回向量属性a"""

        return self.__a

    def set_vec_a(self, a):
        """修改向量属性a"""

        self.__a = a

    def get_vec_b(self):
        """返回向量属性b"""

        return self.__b

    def set_vec_b(self, b):
        """修改向量属性b"""

        self.__b = b

    def get_vec_c(self):
        """返回向量属性c"""

        return self.__c

    def set_vec_c(self, c):
        """修改向量属性c"""

        self.__c = c

    def __add__(self, other):
        """重写加运算"""

        return Vector(self.__a + other.__a, self.__b + other.__b, self.__c + other.__c)

    def __sub__(self, other):
        """重写减运算"""

        return Vector(self.__a - other.__a, self.__b - other.__b, self.__c - other.__c)

    def __mul__(self, other):
        """重写乘运算"""

        return Vector(self.__a * other.__a, self.__b * other.__b, self.__c * other.__c)

    def __truediv__(self, other):
        """重写除运算"""

        return Vector(self.__a / other.__a, self.__b / other.__b, self.__c / other.__c)

    def __str__(self):
        """输出对象信息"""

        return "Vector[a : {}, b : {}, c : {}]".format(self.__a, self.__b, self.__c)


if __name__ == "__main__":
    v1 = Vector(1, 1, 1)
    v2 = Vector(2, 3, 4)
    print(v1)
    print(v2)
    print("v1 + v2 = {}".format(v1 + v2))
    print("v1 - v2 = {}".format(v1 - v2))
    print("v1 * v2 = {}".format(v1 * v2))
    print("v1 / v2 = {}".format(v1 / v2))
