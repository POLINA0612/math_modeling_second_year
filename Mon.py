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
            self.state = self.states[1]
        elif self.state == self.states[1]:
            self.state = self.states[2]
        elif self.state == self.states[2]:
            self.state = self.states[3]
    
    def is_ripe(self):
        if self.state == self.states[3]:
            print('Можно собирать урожай')
            return True
        else:
            return False


class Tomato_bush:
    def __init__(self, n):
        self.n = n
        self.tomatoes = [Senior_tomato() for i in range(self.n)]
    
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    
    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True
    
    def give_away_all(self):
        if self.all_are_ripe():
            self.tomatoes = []
            print('Собрали урожай.')
        else:
            print('Помидоры еще не созрели.')
            

class Gardener:
    def __init__(self):
        self.name = 'Грагас'
        self.plant = Tomato_bush(10)
    
    def work(self):
        self.plant.grow_all()
    
    def harvest(self):
        if self.plant.all_are_ripe():
            print('Собираем урожай')
            self.plant.give_away_all()
        else:
            self.knowledge_base()
    
    def knowledge_base(self):
        print('Справка по садоводству (для дебилов)')
        print('1.Выберите подходящее место для выращивания помидоров. Они нуждаются в большом количестве солнечного света')
        print('2.Подготовьте почву для помидоров: разрыхлите почву и удобрите её органическими веществами.')
        print('3.Следите за поливом. Помидоры нуждаются в регулярном поливе. Но не вздумайте переусердствовать.')
        print('4.Обрезайте растения. Чтобы помидоры росли крупными и здоровыми, необходимо обрезать лишние листья и побеги.')
        print('5.Защитите растения от вредителей и болезней.')
        print('Удачи в выращивании помидоров!')


gardener = Gardener()
gardener.work()
gardener.harvest()