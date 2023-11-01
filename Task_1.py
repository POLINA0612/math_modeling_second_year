from random import randint 
class Human:
    default_name = input()
    default_age = input()
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._own_home = 0
        self._money = input()

    def info(self):
        print(self.name)
        print(self.age)
        print(self._money)
    
    def _make_deal(self, house):
        self._own_home += 1
        self._money -= house._price
    
    def earn_money(self):
        self._money += randint(100000, 99999999)
    
    def buy_house(self, house):
        if self._money - house._price > 0:
            self._make_deal()
    

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    
    def final_price(self, price):
        self.price = price * (1 - 0,35)
    

class SmallHouse(House):
    def __init__(self, area, price):
        super().__init__(area, price)
        self.area = 40

human = Human()

