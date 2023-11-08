class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __str__(self):
        return f'Название системы {self.name} и её планеты {[i for i in self.planets]}'
    
system_1 = StarSystem(['planet_1', 'planet_2'], 'System_1')
print(system_1)