# postional value(*)
# keyword argument(**)

def hello (name,age=21):
    print("Hello "+ name + ", you are " + str(age) + " years old.")
#Here (name -> positional argument, age-> keyword argument )


#hello("ATG",24)

def hello(*args,**kwargs):
    print(args)
    print(kwargs)

#hello("ATG","learner",age=22,dob=1989)

lst=list(('ATG', 'learner'))
dict_val={'age': 22, 'dob': 1989}

hello(lst,dict_val)
#considering both as a postional argument

hello(*lst,**dict_val)
#considering (first as postional argument,second as keyword argument)

hello("ATG","NEPALI",age=22,dob =1532 )