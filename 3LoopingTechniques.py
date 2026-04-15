dict1 = {1 : "One", 2 : "Two"}
for k,v in dict1.items():
    print(f"The key is {k} and value is {v}")

for i,v in enumerate(['Apple', 'Banana', 'Pear']):
    print(f"The index is {i} and value is {v}")

li1 = [1, 2, 3, 4]      # Same can be done for tuple
li2 = ["ONE", "TWO", "THREE", "FOUR"]       # Same can be done for tuple
for x,y in zip(li1, li2):
    print(f"li1 elem {x} and li2 elem {y}")

# Reverse loop on a sequence
for i in reversed(range(10)):
    print(f"The value is {i}")

# Sorted list
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for y in sorted(basket):
    print(f"The sorted elements are {y}")

uniq_basket = list(set(basket))
print(uniq_basket)