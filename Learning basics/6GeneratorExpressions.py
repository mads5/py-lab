from sys import getsizeof

def my_gen():
    '''When you call a normal function with a return statement the function is terminated whenever it 
    encounters a return statement. In a function with a yield statement the state of the function is 
    “saved” from the last call and can be picked up the next time you call a generator function.'''

    """yield : To pause a function midway and resume from where the function was paused, you use the yield statement"""
    """When a function contains at least one yield statement, it’s a generator function."""

    for i in range(5):
        yield i

def generator_iteration():
    #print(my_gen.__doc__)
    g = my_gen()
    print(g)
    print(g.__next__())     # yield next value
    print(g.__next__())     # yield next value
    print(next(g))          # yield next value : Another format, any of these can be used
    print(next(g))
    print(next(g))
    #print(next(g))          # This will throw StopIteration

#generator_iteration()

list_compre = [x for x in range(1000)]
generator_compre = (x for x in range(1000))
#print(list_compre)
#print(generator_compre)

def compare_list_gen():
    # Saves memory for large sequence as it gets obj on demand, but as it saves context, it is bit slow
    print(f"The size of list comprehension : {getsizeof(list_compre)}")
    print(f"The size of gen comprehension : {getsizeof(generator_compre)}") 

    # Print the values of generator using generator function
    print("Print the values of generator using generator function : ")
    print(next(generator_compre))
    print(next(generator_compre))
    print(next(generator_compre))

#compare_list_gen()

def greeting():
    print('Hi!')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3


gen_obj_iter = greeting()


while True:
    try:
        print(f"-------{next(gen_obj_iter)}")
    except StopIteration:
        break

### Use case of generator : Reading large files "MemoryError" ###
def csv_reader():
    count = 0
    #for row in open("C:\\Users\\skalantri\\Desktop\\python_prep\\prep\\PythonVariables.py", 'r'):
    for row in open(r"C:\Users\skalantri\Downloads\zulu17.50.19-ca-jdk17.0.11-linux_x64.tar.gz", 'r+b'):
        count = count + 1
        #yield row
    return count

import time
print(f"Start loop count : {time.localtime()}")
print(csv_reader())     #This method taking 1 sec
print(f"Done loop count : {time.localtime()}")
#print(next(csv_reader()))
#OR using generator comprehension
print(f"Start generator count : {time.localtime()}")
row_count = sum(1 for row in open(r"C:\Users\skalantri\Downloads\zulu17.50.19-ca-jdk17.0.11-linux_x64.tar.gz", 'r+b'))
print(f"Row count : {row_count}")       # This method taking less than a second
print(f"stop generator count : {time.localtime()}")

#ANother way
csv_gen = (row for row in open("C:\\Users\\skalantri\\Desktop\\python_prep\\prep\\PythonVariables.py", 'r'))
print(next(csv_gen))

## Applying functions to generator expressions
m = sum(i * i for i in range(10, 1, -1))
print(m)
