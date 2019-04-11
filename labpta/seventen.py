# 7-10

def statsScoreInfo():
    """统计平均成绩以及不及格人数"""

    averScore = 0.0  # 平均成绩
    failStuNum = 0  # 不及格学生人数
    sumStuNum = 0  # 学生总人数
    sumScore = 0.0  # 学生成绩总和
    inputScore = 0.0  # 待输入成绩

    while inputScore >= 0.0:
        inputScore = float(input())

        if inputScore >= 0.0:
            sumStuNum += 1
            sumScore += inputScore

        if inputScore < 60.0 and inputScore >= 0.0:
            failStuNum += 1

    if sumStuNum == 0:
        print("没有学生")
    else:
        averScore = sumScore / sumStuNum
        print("平均分={:.2f},不及格人数={}".format(averScore, failStuNum))


if __name__ == "__main__":

    statsScoreInfo()
