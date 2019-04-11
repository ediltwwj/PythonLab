# 7-6

def addSubMultDivOperation(operatorA, operatorB):
    """实现两个正整数的加减乘除运算"""

    # 变量后加下划线代表变量值通过形参得到
    operatorA_ = int(operatorA)
    operatorB_ = int(operatorB)

    print("{} + {} = {}".format(operatorA_, operatorB_, operatorA_ + operatorB_))
    print("{} - {} = {}".format(operatorA_, operatorB_, operatorA_ - operatorB_))
    print("{} * {} = {}".format(operatorA_, operatorB_, operatorA_ * operatorB_))
    print("{} / {} = {}".format(operatorA_, operatorB_, operatorA_ // operatorB_))


if __name__ == "__main__":

    opA = input()
    opB = input()
    addSubMultDivOperation(opA, opB)  # 变量类型交由调用函数去判断
