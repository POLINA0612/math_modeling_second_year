def divide(a, b):
	#assert test, data
    assert b != 0, "Делитель не может быть нулем"
    return a / b

print(divide(10, 2))
print(divide(10, 0))