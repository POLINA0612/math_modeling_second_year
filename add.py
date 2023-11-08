class Number:
    def __init__(self, value):
        self.data = value
        
    def __add__(self, other):
        return Number(self.data + other * 7)


a = Number(12)
b = a + 4 + 89
print(b.data)