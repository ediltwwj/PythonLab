"""实验八第三题"""


class ShopComputer:
    def __init__(self, list, money):
        """构造方法，list为商品信息列表，money为开店进货后余额"""

        self.__list = list
        self.__money = money

    def get_computer_list(self):
        """返回商品信息列表"""

        return self.__list

    def get_shop_money(self):
        """返回商店余额"""

        return self.__money

    def search_computer(self):
        """查找商品"""

        list = self.__list
        flag = 0

        brand = input("请输入需要查找的电脑品牌 : ")
        for dict in list:
            if brand in dict.values():
                print("Brand : {}, Amount : {}, Price : {}".format(dict['brand'], dict['amount'], dict['price']))
                flag = 1
                break

        if flag == 0:
            print("对不起，该电脑品牌暂未进货")

    def sell_computer(self):
        """售卖商品"""
        flag = 0

        brand = input("尊敬的顾客，请输入需要购买的电脑品牌 : ")
        for dict in self.__list:
            if brand in dict.values():
                flag = 1

                if dict['amount'] == 0:
                    print("所选品牌电脑暂时无货，我们会及时补货")
                else:
                    dict['amount'] -= 1
                    self.__money += dict['price']
                    print("恭喜你购买成功,已付款{}元".format(dict['price']))

                break

        if flag == 0:
            print("对不起，该电脑品牌暂未进货")

    def buy_computer(self):
        """进货"""

        canBuy = False
        brand = input("请输入您要进货的电脑品牌：")

        for dict in self.__list:
            if brand in dict.values():
                canBuy = True
                break

        if canBuy:
            number = int(input('请输入进货数量：'))
            for dict in self.__list:
                if brand in dict.values():

                    pri = float(input("请输入进货价："))
                    totalPrice =  pri * number
                    print('进货总价为：{}'.format(totalPrice))
                    break

            if totalPrice > self.__money:
                print("对不起，您的金额不足！")
            else:
                self.__money -= totalPrice
                for dict in self.__list:
                    if brand in dict.values():
                        dict['amount'] += number
                        break

        else:
            print('您要进货的品牌不再授权范围内！')

    def __str__(self):
        """输出店铺信息"""

        str = ""
        for dict in self.__list:
            str += "Brand : {}, Amount : {}, Price : {}\n".format(dict['brand'], dict['amount'], dict['price'])

        return str + "Money : {}".format(self.__money)

def main():
    list = [
        {'amount':10,'brand':'爱国者','price':4999},
        {'amount':20,'brand':'外星人','price':6999},
        {'amount':20,'brand':'飞行堡垒','price':4999}]

    shop = ShopComputer(list,20000)
    isExit = True

    while isExit:
        num = int(input("请输入用户类型："))

        if num == 1:
            print("亲爱得顾客，欢迎光临本小店，请选择您要进行的操作：")

            while True:
                print("1、查找商品")
                print("2、购买商品")
                print("3、退出")

                number = int(input())
                if number == 1:
                    shop.search_computer()
                elif number == 2:
                    shop.sell_computer()
                else:
                    break
        if num == 2:
            print("管理员你好！请选择您要进行的操作：")

            while True:
                print("1、店铺进货")
                print("2、查看店铺信息")
                print("3、退出")

                number = int(input())
                if number == 1:
                    shop.buy_computer()
                elif number == 2:
                    print(shop)
                else:
                    break

        if num == 0:
            print("Goodbye ~~~~")
            isExit = False

if __name__ == "__main__":

    main()


