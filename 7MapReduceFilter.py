#The main difference between a map and a filter is the return of values. A map will always have a representation 
# for elements in the list. The filter will filter out the only elements that will meet the conditions in the 
# function
import functools
arr = [0, 1, 2, -3, -4, None]
x = map(bool, arr)
print(list(x))

y = filter(bool, arr)
print(list(y))

arr1 = [1, 2, 10, 3, 4, 5]
# Sum of all elements of arr1
z = functools.reduce(lambda a, b: a + b, arr1)
print(z)

# Get maximum element from arr1
w = functools.reduce(lambda a, b : a if a>b else b, arr1)
print(w)