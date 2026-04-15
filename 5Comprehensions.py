'''List comprehension : A list comprehension consists of brackets containing an expression followed by a for clause, 
 then zero or more for or if clauses.'''

squares = [x*2 for x in range(10) if x % 2 == 0]
print(squares)

list1 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(list1)

# Matrix #####################
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

transpose = [] # [matrix[a][b] for a in range(len(matrix)) for b in range(len(matrix[0]))]
#print(transpose)

for a in range(4):    
    print(f"Loop {a}")
    new_matrix = []
    for row in matrix:
        print(row[a])
        new_matrix.append(row[a])
    transpose.append(new_matrix)

print(transpose)

my_list = [x * 2 for x in range(10)]
print(my_list)

num1 = [1,2]
letters = ['A', 'B']
num_letters = zip(num1,letters)
print(num_letters)

num_letters1 = [[i, j] for i in num1 for j in letters]
print(num_letters1)

for u, v in enumerate(num1):
    print(f"u : {u} and v : {v}")

###### Set comprehensions ######################
set_compre = {x for x in range(10) if x%2!=0}
print(f"Set comprehensions : {set_compre}")


# Dict comprehensions
dict_compre = {x : x**2 for x in range(5)}
print(f"dictionary comprehensions : {dict_compre}")

