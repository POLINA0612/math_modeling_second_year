from random import randint 
class Human:
    default_name = 'Art'
    default_age = 71
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._own_home = 0
        print('Введите материальное состояние:')
        self._money = int(input())

    def info(self):
        print(self.name)
        print(self.age)
        print(self._money)
    
    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)
    
    def _make_deal(self, house):
        self._own_home += 1
        self._money -= house._price
    
    def earn_money(self):
        self._money += randint(100000, 99999999)
    
    def buy_house(self, house):
        if int(self._money) - int(house._price) > 0:
            self._make_deal(house)
    

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    
    def final_price(self, _price):
        self.price = _price * (1 - 0,35)
    

class SmallHouse(House):
    def __init__(self, area, _price):
        super().__init__(area, _price)
        self.area = 40

human = Human('Giorgia', 20)

human.info()
human.default_info()

house = SmallHouse(70, 23534853)
human.buy_house(house)

human.earn_money()

human.buy_house(house)

human.info()