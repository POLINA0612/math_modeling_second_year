def sum_arg(a, b): #Именованная функция
  return a + b

print(sum_arg(12, 25))

#lambda аргумент1, аргумент2, и т.д. : выражение , использующее аргументы

sum_arg = lambda a, b: a + b #Анонимная функция

print(sum_arg(7, 13))

current_list = [1, 6, 4]
new_list = list(map(lambda x: x*2 , current_list))
print(new_list)