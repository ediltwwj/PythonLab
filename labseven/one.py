"""实验七第一题"""

if __name__ == "__main__":

    # 同时输入不同类型的数据
    raw = input("please input an integer, a float and a string : ")
    a, b, c = raw.split()
    a = int(a)
    b = float(b)
    c = str(c)

    # 读入一个复数
    x = complex(input("please input a complex : "))

    # 读入一个字典数据
    dict = {}
    key, value = input("please input a key and a value : ").split()
    dict[key] = value

    print("不同数据类型 ： {}, {}, {}".format(type(a), type(b), type(c)))
    print("复数虚部 ： " + str(x.imag) + "复数实部 : " + str(x.real))
    print("字典 ： ", end="")
    for kv in dict.items():
        print(kv, end="")
