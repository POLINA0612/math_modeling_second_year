from random import randint
class Pyramyd:
    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
        self.current_h = 0

    def add_bricks(self, n):
        self.bricks_count += n

    def get_height(self):
        print(self.current_h)
    
    def is_done(self):
        return int(self.current_h * 100 / self.max_h)

class Builder:
    def __init__(self,n):
        self.day = 1
        self.bricks = n
        self.my_pyramid = Pyramyd(5)
    def buy_bricks(self,n):
        self.bricks += n
    def build_pyramid(self, n):
        if n > self.bricks:
            print('Ни хуя, ни пирамид')
        elif self.bricks <= 15 and self.bricks != 0:
            n = n - randint(1,5)
            print('Строим')
        else:
            print('Мы бомжи без пирамиды')
    def work_day(self):
        self.day += 1
        print('День', self.day,
              'За день', 
              'Количество кирпичей',
              'Процент работы', self.my_pyramid.is_done())
        if self.my_pyramid.is_done() == 100:
            print('Сосите члены')
            return False

b = Builder(15)

while True:
    b.work_day()
    break