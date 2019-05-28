""""实验四第三题"""


if __name__ == "__main__":

    list1 = ["XXXX", "b", 3 ,"c", "&", "a", 3, "3", 3, "aa", "3", "XXXX"]
    list2 = ["e", "f", "g"]
    list3 = list1[1 : -1]


    # 删除特殊符号
    print("删除特殊符号 : ", end="")
    [print(x, end=" ") for x in list3 if str(x).isalnum()]
    print()

    # 统计3在list3中出现的次数
    num = 0
    for x in list3:
        if x == 3:
            num += 1
    print("3在list3中出现的次数 : " + str(num))

    # 去除list3除26个字母以外的元素
    print("去除list3除26个字母以外的元素 : ", end="")
    [print(x, end=" ") for x in list3 if str(x).isalpha() and len(x) == 1]
    print()

    # 对list3进行排序，先分离不同数据类型
    print("对list3进行排序 : ", end="")
    num = [x for x in list3 if type(x) is int]
    word = [x for x in list3 if type(x) is str]
    num.sort()
    word.sort()
    sort_list3 = num + word
    print(sort_list3)

    # 在末尾追加'd',并把list2追加到list3
    print("在末尾追加'd',并把list2追加到list3 : ", end="")
    list3.append('d')
    list3 = list3 + list2
    print(list3)

    # list3追加变量('h'),和('h'),观察区别
    a = ('h',)
    list3.append(a)

    b = ('h')
    list3.append(b)

    # 将list3转换为元组
    t1 = tuple(list3)
    print("转换后的数据类型 : " + str(type(t1)))

    # 打印'h'的索引
    print("输出'h'的索引 : " + str(t1.index(('h',))))



