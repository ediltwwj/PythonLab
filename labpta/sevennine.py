# 7-9

def binLeapYear(year):
    """输出一个年份是不是闰年"""

    assert year > 0, "Value must be valid"

    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print("{}是闰年".format(year))
    else:
        print("{}不是闰年".format(year))


if __name__ == "__main__":

    year = int(input())
    binLeapYear(year)
