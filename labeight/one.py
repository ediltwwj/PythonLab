"""实验八第一题"""


class Person:

    def __init__(self, name, id, sex):
        """父类构造方法"""

        self.__name = name
        self.__id = id
        self.__sex = sex

    def get_name(self):
        """返回名字"""

        return self.__name

    def set_name(self, name):
        """修改名字"""

        self.__name = name

    def get_id(self):
        """返回ID"""

        return self.__id

    def set_id(self, id):
        """设置ID"""

        self.__id = id

    def get_sex(self):
        """返回性别"""

        return self.__sex

    def set_sex(self, sex):
        """设置性别"""

        self.__sex = sex

    def __str__(self):
        """输出对象信息"""

        return "Name : {}, ID : {}, Sex : {}".format(self.__name, self.__id, self.__sex)


class Student(Person):

    def __init__(self, name, id, sex, major):
        """子类构造方法"""

        Person.__init__(self, name, id, sex)
        self.__major = major

    def get_major(self):
        """返回专业"""

        return self.__major

    def set_major(self, major):
        """设置专业"""

        self.__major = major

    def __str__(self):
        """输出对象信息"""

        return super().__str__() + ", Major : {}".format(self.__major)


if __name__ == "__main__":
    p = Person("Person", 1001, 'M')
    print(p)
    s = Student("Student", 1005, 'M', "rg")
    print(s)
