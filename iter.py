	
a = range (3) # range допускает множество итераторов
# next(a)
print(id(a))
 
new_a = iter(a)
print(id(new_a))
 
print(next (new_a))
print(next (new_a))
print(next (new_a))