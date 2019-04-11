# 7-2

def binTriangle(sideA, sideB, sideC):
    """判断三条边是否能够构成三角形"""

    assert sideA > 0. and sideB > 0. and sideC > 0., \
        "Side value must be valid"

    if (sideA + sideB > sideC) and (sideA + sideC > sideB) and (sideB + sideC > sideA):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":

    sideA, sideB, sideC = map(float, input().split())
    binTriangle(sideA, sideB, sideC)
