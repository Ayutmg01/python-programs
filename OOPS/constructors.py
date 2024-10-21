# Interview Question: Can we you use multiple __init__ /contructor in python ?
# answer-> yes but u need to initialize (*args) first 
# disadvantage = u need to define many conditions ( not a good practice)

class Animal:
    def __init__ (self, *args):
        if len(args)==1:
            self.name = args[0]
        elif len(args)==2:
            self.name= args[0]
            self.species=args[1]
        elif len(args)==3:
            self.name=args[0]
            self.species = args[1]
            self.age= args[2]

   
    def make_sound(self,sound):
        return "The animal is {} and says {} ".format(self.name, sound)
    
dog=Animal("dog","mammal",14)
print(dog.name)
print(dog.species)
print(dog.age)
print(dog.make_sound("woof woof"))