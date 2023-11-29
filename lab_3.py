def square_root(x):
    if x < 0 and x != -1:
        raise ValueError('Нельзя извлекать корень из отрицательного числа')
    elif x == -1:
        print(-1)
        print('Я мнимая единица, мне можно всё')
    else:
        print(x ** 0.5)

square_root(33)