if __name__ == "__main__":

    a = ['name', 'age', 'sex']
    b = ['Dog', 38, 'Male']

    new_dict = dict(zip(a, b)) # 方法1

    print("方法1")
    for key, value in new_dict.items():
        print(str(key) + " : " + str(value))  # 类型转换避免键值对是非字符串类型

    new_dict_2 = {} # 方法2
    for i in range(len(a)):
        new_dict_2[str(a[i])] = str(b[i])

    print("方法2")
    for key, value in new_dict_2.items():
        print(key + " : " + value)


