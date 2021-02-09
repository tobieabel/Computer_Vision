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
#generator functions - use of Yield key word
def gen(lst):
    for i in lst:
        print ("next number is ")
        yield i

result = gen(list)
print(next(result))


