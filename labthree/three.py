"""实验三第三题"""

if __name__ == "__main__":

    while True:
        n, m = map(int, input("input two integer n and m(n < m < 106) : ").split(' '))
        if n == 0 and m == 0:
            break;

        sum = 0
        for i in range(n, m + 1):
            sum += 1 / i ** 2

        print("Result : {: .5f}".format(sum))
