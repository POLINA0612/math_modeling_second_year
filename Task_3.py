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
            return 1
        return 0



class Tomato_bush:
    def __init__(self, n):
        self.n = n
        self.tomatoes = [Senior_tomato() for i in range(self.n)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        k = 0
        for tomato in self.tomatoes:
           if tomato.is_ripe() == 1:
                k += 1
        if k == len(self.tomatoes):
            print('Папой клянусь, всё созрело')
            return True
        return False
    def give_away_all(self):
        if self.all_are_ripe() == 1:
            self.tomatoes = []
            print('Собрали урожай.')


class Gardener:
    def __init__(self):
        self.name = 'Грагас'
        self.plant = Tomato_bush(10)
    def work(self):
        for tomato in self.plant.tomatoes:
            tomato.grow()
    def harvest(self):
        if self.plant.all_are_ripe():
            print('Собираем урожай')
        else:
            self.knowledge_base()
    def knowledge_base(self):
        print('Справка по садоводства (для дебилов):')
        print('1.Выберите подходящее место для выращивания помидоров. Они нуждаются в большом количестве солнечного света.')
        print('2.Подготовьте почву для поимдоров: разрыхлите почву и удобрите её органическими веществами.')
        print('3.Следите за поливом. Помидоры нуждаются в регулярном поливе. Но не вздумайте переусердствовать.')
        print('4.Обрезайте растения. Чтобы помидоры росли крупными и здоровыми, необходимо обрезать лишние листья и побеги.')
        print('5.Защитите растения от вредителей и болезней.')
        print('Удачи в выращивании помидоров!')


Gardener.knowledge_base(1)
g = Gardener()
g.work()
g.harvest()