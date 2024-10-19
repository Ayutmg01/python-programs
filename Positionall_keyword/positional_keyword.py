def hello (name,age=21):
    print("Hello "+ name + ", you are " + str(age) + " years old.")


hello("ATG",24)

def hello(*args,**kwargs):
    print(args)
    print(kwargs)

hello("ATG","learner",age=22,dob=1989)