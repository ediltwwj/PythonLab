# 7-8

def binEvenNumber(number):
    """输出一个数是否是偶数"""

    if number % 2 == 0:
        print("{}是偶数".format(number))
    else:
        print("{}不是偶数".format(number))


if __name__ == "__main__":

    number = int(input())
    binEvenNumber(number)
