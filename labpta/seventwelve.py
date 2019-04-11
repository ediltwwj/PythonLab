# 7-12

def evenNumberCumulative():
    """求1-n所有偶数的积"""

    number = int(input())
    cumulaRes = 1  # 积的结果

    for iter in range(1, number + 1):
        if iter % 2 == 0:
            cumulaRes *= iter

    print(cumulaRes)


if __name__ == "__main__":
    
    evenNumberCumulative()
