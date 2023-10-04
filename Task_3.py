class Senior_tomato:
    states = {0: "Нет помидоров",
                1: "Цветение",
                2: "Зелёные помидоры",
                3: "Красные помидоры"}
    def __init__(self):
        self.index = 0
        self.state = self.states[0]
    def grow(self):
        if self.state == self.states[0]:
            self.state == self.states[1]
        elif self.state == self.states[1]:
            self.state == self.states[2]
        elif self.state == self.states[2]:
            self.state == self.states[3]
    def is_ripe(self):
        if self.states == self.states[3]:
            print('Можно собирать урожай')


class Tomato_bush:
    def __init__(self, n):
        self.n = n
        self.tomatoes = [Senior_tomato]
    def grow_all(self, n):
        Senior_tomato.grow(n)
    def all_are_ripe(self):
        if Senior_tomato.is_ripe(self) == 1:
            print('Папой клянусь, всё созрело')
            return True
    def give_away_all(self):
        if self.all_are_ripe() == 1:
            self.tomatoes = []
            print('Собрали урожай.')


class Gardener:
    def __init__(self):
        self.name = 'Грагас'
        self.plant = Tomato_bush
    def work(self, n):
        Senior_tomato.grow(n)
    def harvest(self, n):
        if self.tomatoes == [i for i in range(n)]