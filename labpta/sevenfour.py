# 7-4

def printHelloInfo(name):
    """输入一个姓名，输出问候信息"""

    print("Hello," + name.capitalize() + "!")  # 只有遇见英文字母才会首字母大写，其余不变


if __name__ == "__main__":

    name = input()
    printHelloInfo(name)
