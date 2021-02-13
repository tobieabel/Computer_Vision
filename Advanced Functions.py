#some advanced python functionality taken from scipy-lectures -
#https://scipy-lectures.org/advanced/advanced_python/index.html

#a list comprehension is actually a 'generator expression', meaning a function that generates a sequence of reulsts, not a single value
list = [1,2,3,4]
it = (i for i in list)#creates just the generator sequence, not an actual list
print(it)
for i in it:
    print (i)
list2 = [i for i in list]#creates a formal list from the generator
print(list2)
list3 = {i:i + 1 for i in list}#creates a dictionary
print(list3)
#generator functions - use of Yield key word means instead of running the entire loop in the function
#, the control is 'yielded' back to the caller when the yield word is encountered.  The state of the function is stored in
#the 'result' variable, and this can then be passed back to the function with the use of the 'next' keyword
#which picks up the function where it left of, until the next 'yield' is encountered
def gen(lst):
    for i in lst:
        print ("next number is ")
        x = yield i
    yield x * 2

result = gen(list)
print(result)
print(next(result))
print(result.__next__())#just showing that next is a standard dunnder method of the generator class
print(next(result))
print(next(result))
print(result.send(10))#sends the value 10 to the x variable currently assigned to 'yield'

#Decorators, any funtion which takes as an argument another function, and then modifies that functions behavour
#The decorator function is declared in the normal function way
#below is the equivalent of a decorator, a wrapper called as part of another function
def Decorator_Function(func):
    def wrapper(*args, **kwargs):#This means the function accepts any number of arguments or keyword argumments
        print('This is the wrapper talking')
        func(*args, **kwargs)#use any arguments or keyword arguments passed by the normal function
        print('This is the decorator talking')
        return (func(*args, **kwargs))#This ensures any return values from the normal function are repected by the decorator
    return wrapper
#create a normal function
def Normal_Function(word):
    print (word)

Normal_Function = Decorator_Function(Normal_Function)#assign the variable Normal Function to the decorator, which in turn calls the Normal Function function
Normal_Function('Hi')#calling Normal Function now actuall calls the variable linked to the Decorator Function
print(Normal_Function)
#We can achieve the same thing with the decorator syntax.
@Decorator_Function
def Another_Normal_Function(word):
    print (word)
    return 10
result = Another_Normal_Function('Goodbye')#'Goodbye' is an exmaple of passing *arg to the decorator
print(result)#should print the return value from 'Another_Normal_Function', even though its gone through a decorator
