"""实验七第二题"""

if __name__ == "__main__":

    a = [1., 2., 3.]
    print("使用%进行输出 ：")
    print("x       x*x     x*x*x")
    for i in a:
        print("%-8.2f%-8.2f%-8.2f"%(i, i*i, i*i*i))

    print("使用format进行输出 ：")
    print("x       x*x     x*x*x")
    for i in a:
        print("{:<8.2f}{:<8.2f}{:<8.2f}".format(i, i*i, i*i*i))