# 7-3

def integerJoin(number, joinTime):
    """读入整数number，拼接joinTime次，并输出"""

    assert 1 <= number <= 9, \
        "number must between 1 and 9"
    assert 1 <= joinTime <= 10, \
        "joinTime must between 1 and 10"

    intStr = ""

    for cur_iter in range(joinTime):
        intStr += str(number)

    print(intStr)


if __name__ == "__main__":

    number, joinTime = map(int, input().split(","))
    integerJoin(number, joinTime)
