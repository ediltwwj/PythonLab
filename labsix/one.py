"""实验六第一题"""


def mp_sort(arr, length):
    """对列表进行排序,并输出"""

    for i in range(0, length):
        for j in range(0, i):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    print("After sorted : ", end="")
    for i in range(length):
        print(arr[i], end=" ")


if __name__ == "__main__":

    arr = []

    n = int(input("n = "))
    b = input("input numbers : ")
    b = b.split()
    for i in b:
        t = int(i)
        arr.append(t)

    mp_sort(arr, n)
