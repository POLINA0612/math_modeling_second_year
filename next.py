f = open('example.txt')
	
# print(f.readline())

# print(f.readline())
# print(f.readline())

print(next(f))

print(next(f))

print(next(f))

f2 = open('example_1.txt')

for i in f2 : # Итератор файла
  print(i)