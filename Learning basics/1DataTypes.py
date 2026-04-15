import random

# Integer
def int_data():
    a = 10      # Basic Int with base 10
    b = 0b10    # Binary: base 2
    c = 0o10    # Octal: base 8
    d = 0x10    # Hexadecimal: base 16

    print(a)
    print(b)
    print(type(b))
    print(c)
    print(d)

    print("Get the type")
    print(f"Is 100 a integer ? : {(100).is_integer()} its type is : {type(100)}")
    print(f"Is 10.5 a integer ? : {(10.5).is_integer()} its type is : {type(10.5)}")
    print(f"Type of 10+5j  is : {type(10+5j)}")
    print(complex(2,3))
    print(complex(2))
    print(type(12E4))

    print("Defining with empty params")
    print(int())
    print(float())
    print(complex())

    rand_num = random.randrange(1,6)
    print(f"Get random numbers between 1 and 6 for rolling a dice {rand_num}")

#int_data()

# Strings and characters
def str_data():
    str1 = "hello, there!"
    print(type(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.lower())
    print(str1.islower())
    
    str2 = "\nHello my love! love you!\n"
    print("Strip method : " + str2.strip())
    print(str2.rstrip("you!"))
    print(str2.find("love"))    # First occurance index
    print(str2.find("hate"))  # same as find() but raises ValueError when string is not found
    print(str2[1:5])    #First index 1 is included and 2nd is not
    print(str2.replace("love", "hate"))
    print(str2.split())
    print(len(str2))
    print(str2.endswith("\n"))


#str_data()

#  Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
def list_data():
    rgb = ["Red", "Green", "Blue"]
    rgba = rgb  ##Creates a shallow copy - modifications to rgb affects rgba also
    if(id(rgb) == id(rgba)):
        rgba.append("Alpn")
    print(rgb)

    rgbs = rgb[:] #Creates a deep copy - modifications to rgb do not affect rgbs array
    rgbs[-1] = "Alpha"
    print(rgb)
    print(rgbs)
    print(len(rgb))

    x = [1,2,3]
    y = ['a', 'b', 'c']
    z = [x, y]
    print("Nested lists :")
    print(z)

    x[len(x):] = ["Apple", "Banana"]
    print("x now is : ")
    print(x)
    #This is similar to extend method
    y.extend(['f', 'e', 'c'])
    print(y)
    print(f"Sorted : {sorted(y)}")

    print("Print after remove and pop")
    y.remove('e')
    x.pop(4)
    print(x)
    print(y)
list_data()

#Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing
def tuple_data():
    t = 12, 54, 'hello' # Tuple packing
    print(t)
    # Nested tuple
    u = t,(1, 2, 3)
    print(u)

    v = t, [1, 2, 3]
    print(v)
    # TypeError: 'tuple' object does not support item assignment 
    # v[0][1] = 0
    # But it can contain mutable objects which can be updated
    v[1][1]= 11
    print(v)

    new_tuple = ()
    new_tuple1 = ("Apple",) # If you dont add comma at the end, it becomes a string
    print(new_tuple)
    print(type(new_tuple1))

    x, y ,z = t     # Tuple/sequence unpacking, needs exact number of elements as of t
    print(z)

    husbands = ['Mike', 'Charles', 'John']
    wives = ['Monica', 'Chistrini', 'Jenny']
    pairs = zip(husbands, wives)            # zip function in Python is used to combine multiple iterables into a single iterable
    print(f"Zip function out : {tuple(pairs)}")

#tuple_data()

# A set is an unordered collection with no duplicate elements
# Basic uses include membership testing, eliminating duplicate entries and mathematical operations
def sets_data():
    set1 = {"Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"}
    if("Violet" in set1):
        print("Violet color is present in rainbow")
    
    set2= set('abdgdubkd')
    set3= set('aaaaazy')
    print(set3)         # No duplicates in a set
    print(set2-set3)    #letters in set2 but not in set3
    print(set2|set3)    #letters in set2 or in set3
    print(set2^set3)    #letters in set2 or set3 but not both
    print(set2&set3)    #letters in set2 and set3 both

    set4= set('1234')
    print(set4)

#sets_data()

#dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. 
#Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
def dict_data():
    dict1 = dict()
    print(dict1)
    dict1["A"] = "Apple"
    print(dict1)

    dict2 = {'B': 'Ball', 'C' : "Cat"}
    dict2['D'] = "Dog"
    print(dict2)
    print(list(dict2))
    
    if('A' in dict2):
        print("A id the key of dict2")
    else:
        print("A is not the key of dict2")
    
    dict3 = dict([(1, "One"), (2, "Two")])
    print(dict3)

#dict_data()