import numpy as np
u = 0
def calculate_area( shape, *args):
    if shape not in ['круг', 'квадрат', 'прямоугольник', 'треугольник']:
        raise ValueError('Неверное название фигуры')
    elif ((len(args) != 1 and (shape == 'круг' or shape == 'квадрат')) or (len(args) != 2 and shape == 'прямоугольник') or (len(args) != 3 and shape == 'треугольник')):
        raise TypeError('Неверное количество аргументов')
    elif shape == 'круг':
        print(np.pi * args[0] ** 2)
    elif shape == 'прямоугольник':
        print(args[0] * args[1])
    elif shape == 'треугольник':
        u = (args[0] + args[1] + args[2]) / 2
        print(((u - args[0]) * (u - args[1]) * (u - args[2])) ** 0.5)
    elif shape == 'квадрат':
        print(args[0] ** 2)
    elif args[0] < 0 or args[1] < 0:
        raise ValueError('Нужны положительные числовые аргументы')

calculate_area('треугольник', 5, 7, 8)
    