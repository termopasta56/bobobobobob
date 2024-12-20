class Human:
    def __init__(self, name='human'):
        self.name = name
        
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
        
    def add_passenger(self, human):
        self.passengers.append(human)
        
    def print_passengers_names(self):
        if self.passengers != []:
            print(f'Names of {self.brand} products')
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f'There are no passengers in {self.brand}')
tomatoes = Human('Tomatoes')
apples = Human('Apples')
car = Auto('shopping cart')
car.add_passenger(tomatoes)
car.add_passenger(apples)
car.print_passengers_names()