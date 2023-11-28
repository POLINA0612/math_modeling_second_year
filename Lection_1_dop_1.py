# Задача заключается в создании имитации движения автомобиля и велосипеда.

# 1. Создайте базовый класс `Vehicle`, который будет иметь следующие методы:
#    - `__init__`: принимает название транспорта и инициализирует список движений и время.
#    - `_move`: имитирует движение транспорта, записывает движение в список и увеличивает время.
#    - `get_moves`: возвращает список движений.
#    - `get_time`: возвращает общее время движения.

# 2. Создайте два дочерних класса `Car` и `Bicycle`, которые наследуют от `Vehicle`.

# 3. В методе `_move` каждого из дочерних классов вызывайте метод `_move` базового класса, а затем добавляйте в список движений сообщение о движении.

# 4. Создайте два объекта классов `Car` и `Bicycle`.

# 5. Для каждого из объектов выполните три движения, выведите сообщения о движении и выведите список движений и общее время движения для каждого объекта.


import time

class Vehicle:
    def __init__(self, name):
        self._name = name
        self._moves = []
        self._time = 0.

    def _move(self):
        start_time = time.time()
        self._moves.append(self._name + ' is moving.')
        time.sleep(1)  # Simulate time spent moving
        end_time = time.time()
        self._time += end_time - start_time

    def get_moves(self):
        return self._moves

    def get_time(self):
        return self._time

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def _move(self):
        super()._move()
        return self._name + ' is moving.'

class Bicycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def _move(self):
        super()._move()
        return self._name + ' is moving.'

car = Car('Tesla')
bicycle = Bicycle('BMX')

for _ in range(3):
    print(car._move())
    print(bicycle._move())

print(car.get_moves())
print(bicycle.get_moves())
print(car.get_time())
print(bicycle.get_time())