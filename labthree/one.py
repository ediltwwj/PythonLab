"""实验三第一题"""

if __name__ == "__main__":

    sum = 0

    for i in range(100, 1001):
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
        if flag ==1:
            sum += i

    print("100-1000的素数之和 : {}".format(sum))
