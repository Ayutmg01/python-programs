## inheritance
#car class blueprint 

class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    def selfdriving(self):
        print("It is a self driving car")

    def driving(self):
        print("Car is used for driving")

# Audi Car is inheriting form the car class
class Audi(Car):
    def __init__(self, windows, doors, enginetype, horsepower):
        super().__init__(windows, doors,enginetype)
        self.horsepower= horsepower

audiq7=Audi(4,5,"Disel", 450)

print(audiq7.horsepower)
print(audiq7.windows)
audiq7.selfdriving()


car1 =Car(4,5,"disel")
print(car1)
print(audiq7)

print(dir(audiq7))
print(dir(car1))