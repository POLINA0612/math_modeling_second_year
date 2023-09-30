from random import randint
class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.h = max_h
        self.current_h = 0
        self.all_bricks = 0

    # def add_bricks(self):
    #      self.all_bricks += b.work_day.a()

    def get_height(self):
        if self.all_bricks % 5 >= 0:
            self.current_h += 1
            self.all_bricks //= 5
        print(self.current_h)

    def is_done(self):
        return int(self.current_h * 100 / self.max_h)

class Builder:
    def __init__(self, max_h,n):
        self.day = 1
        self.bricks = n
        self.my_pyramid = Pyramid(15)
        self.max_h = max_h
        self.h = max_h
        self.all_bricks = 0
        
    def buy_bricks(self):
        self.bricks += 15 - self.bricks
    def build_pyramid(self, n):
        if self.all_bricks % 5 > 0 and self.bricks + (self.all_bricks % 5) <= 15:
            self.bricks += self.all_bricks % 5
            self.all_bricks == 0
            return False
        elif n > self.bricks:
            print('Нет пирамиды')
            self.buy_bricks()
            return False
        elif self.bricks >= 15 and self.bricks == 0:
            print('Научись считать от одного до пяти, придурок')
        elif self.bricks - (self.all_bricks % 5) <= 15:
            self.bricks -= n
            # self.my_pyramid.add_bricks()
            print('Типо строим')
            return True
    def work_day(self):
        while self.my_pyramid.is_done() != 100:
            a = randint(1, 5)
            self.all_bricks += a
            if a > self.bricks:
                self.build_pyramid(a)
                print('День', self.day)
                print('За день', a, 'положили кирпичей')
                print('Докупили', 15 - self.bricks - a, 'кирпичей')
                print('Количество кирпичей', self.bricks)
                print('Готовность работы', self.my_pyramid.is_done())
                self.day += 1
                self.my_pyramid.get_height()
                print()
            elif a + (self.all_bricks % 5) <= 5:
                self.build_pyramid(a)
                print('День', self.day)
                print('За день', a, 'положили кирпичей' )
                print('Количество кирпичей', self.bricks)
                print('Готовность работы', self.my_pyramid.is_done())
                self.day += 1
                self.my_pyramid.get_height()
                print()
            elif self.my_pyramid.max_h < self.my_pyramid.current_h:
                print('Помянем')
            
            
        self.exit()
    def exit(self):
        print('Офигеть, вышло')

b = Builder(15,15)

while True:
    b.work_day()
    break