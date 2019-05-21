import random

"""实验五第二题"""


def set_practice(num):
    """集合的去重和排序"""

    s = set()  # 注意不能使用{}生成空集合

    for i in range(num):
        s.add(random.randint(1, 1000))  # 自动去重

    print(sorted(s))  # 不覆盖原集合，返回新集合


if __name__ == "__main__":
    num = int(input("请输入随机数个数 ："))
    set_practice(num)