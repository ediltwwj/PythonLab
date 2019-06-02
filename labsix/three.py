"""实验六第三题"""


def my_feb(n):
    """返回斐波那契的第n个元素"""

    if n == 1 or n == 2:
        return 1
    else:
        return my_feb(n - 1) + my_feb(n - 2)


if __name__ == "__main__":
    n = int(input("请输入斐波那契数列的索引 : "))
    print("结果为 ： {}".format(my_feb(n)))
