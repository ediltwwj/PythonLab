# 7-11

def calcuCpBestStature():
    """为用户计算他/她的情侣的最佳身高"""

    peopleNumber = int(input())  # 用户数量

    for iter in range(peopleNumber):
        peopleData = input()
        peopleSex, peopleStature = peopleData.split()
        peopleSex = str(peopleSex)  # 性别
        peopleStature = float(peopleStature)  # 身高

        assert peopleSex == 'M' or peopleSex == 'F', \
            "The value of peopleSex is illegal(M or F)"
        assert peopleStature >= 0.0 and peopleStature <= 3.0, \
            "The value of peopleStature is illegal(1.0,3.0)"

        if peopleSex == 'F':
            print("{:.2f}".format(peopleStature * 1.09))
        else:
            print("{:.2f}".format(peopleStature / 1.09))


if __name__ == "__main__":

    calcuCpBestStature()
