from random import randint
class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.h = max_h
        self.bricks_count = 0
        self.current_h = 0

    def add_bricks(self, n):
        self.bricks_count += n

    def get_height(self):
        print(self.current_h)
    
    def is_done(self):
        return int(self.current_h * 100 / self.max_h)

class Builder:
    def __init__(self, max_h, n):
        self.day = 1
        self.bricks = n
        self.my_pyramid = Pyramid(15)
        self.max_h = max_h
        self.h = max_h
        
    def buy_bricks(self):
        n = randint(1,5)
        if self.bricks + n <= 15:
            self.bricks += n
    def build_pyramid(self, n):
        n = randint(1,5)
        if n > self.bricks:
            print('Нет пирамиды')
            self.buy_bricks()
            return False
        elif self.bricks >= 5 and self.bricks == 0:
            print('Научись считать от одного до пяти, придурок')
            return False
        else:
            self.bricks -= n
            self.my_pyramid.add_bricks(n)
            print('Типо строим')
            return False
    def work_day(self):
        while self.my_pyramid.is_done() != 100:
            self.day += 1
            a = randint(1, 5)
            if self.my_pyramid.max_h < self.my_pyramid.h:
                print('Помянем')
            else:
                print('День', self.day,
                    'За день', a, 'кирпичей', 
                    'Количество кирпичей', self.bricks,
                    'Готовность работы', self.my_pyramid.is_done())
            self.build_pyramid(a)
            print()

b = Builder(15,15)

while True:
    b.work_day()
    break