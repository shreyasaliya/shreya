a = 9
b = 10
c = sum((a,b))  #built in function
print(c)

def function1():
    print("hello you are in function1")
function1()

def function2(a,b):
    print("hello you are in function2", a+b)
function2(5,7)

def function3(a,b):
    """This is a function which will calculate average of two numbers
       This function doesn't work for three numbers"""  #doc string
    average =(a+b)/2
    # print(average)
    return average
v = function3(5,7)
print(v)

#print doc string
print(function3.__doc__)