"""实验六第二题"""


def check(arr):
    """返回传入列表或者元组的奇数位值"""

    length = len(arr)
    temp = []

    for i in range(0, length, 2):
        temp.append(arr[i])

    return temp


if __name__ == "__main__":
    test_list = [10, 15, 17, 12, 5, 8, 11]
    result_list = check(test_list)
    print("原数组 : {}".format(test_list))
    print("奇数索引数组 : {}".format(result_list))
