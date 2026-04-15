import numpy as np
"""What is NumPy?
NumPy (Numerical Python) is an open source Python library that’s widely used in science and engineering. 
The NumPy library contains multidimensional array data structures, such as the homogeneous, N-dimensional
 ndarray, and a large library of functions that operate efficiently on these data structures."""

'''Most NumPy arrays have some restrictions. For instance:
1. All elements of the array must be of the same type of data.
2. Once created, the total size of the array can’t change.
3. The shape must be “rectangular”, not “jagged”; e.g., each row of a two-dimensional array must have 
the same number of columns.'''

# axis=0 : Applicable to rows functionality
# axis=1 : Applicable to columns functionality

a = np.array([
    [1,2,3],
    [4,5,6]
])

x = np.array([1, 2, 3, 4, 5])
print(x[0])
y = x[2:]   #Creates a view which can modify original list x as well
print(y)
y[0] = 20
print(x)

def array_attributes(ar):
    print(f"-----Attributes of array {ar} are : ")
    print(ar.size)   # Total number of elem
    print(ar.ndim)   # Number of dimensions
    print(ar.shape)   #Matrix dimensions will be printed : 2,3
    print(ar.dtype)  #Datatype of array elem

#array_attributes(a)

def basic_array_create():
    zeros_arr = np.zeros(2,dtype=np.int64)
    print(f"Zeros array : {zeros_arr}")
    empty_arr = np.empty(2)     #Preferred as this is faster than zeros()
    print(f"Empty w random elem {empty_arr}")
    arange_arr = np.arange(2,9,2)
    print(f"Arragned array : {arange_arr}")

#basic_array_create()

def reshape_array():    
    arr_org = np.array([1,2,3,4,5,6])
    arr_reshape = arr_org.reshape(3,2)
    print(f"Org array : {arr_org} with shape : {arr_org.shape} \n Reshaping array : {arr_reshape} with shape : {arr_reshape.shape}") #will give a new shape to an array without changing the data, should fit into desired metrix though

    a1 = a[np.newaxis]      #will increase the dimensions of your array by one dimension
    print(f"New axis add : {a1}, Shape : {a1.shape}")
    a2 = a1[np.newaxis]
    print(f"Again New axis add : {a2}, SHape : {a2.shape}")

    a_new = np.array([1,2,3,4,5,6])
    print(f"array {a_new} with shape {a_new.shape}")
    b = np.expand_dims(a_new, axis=1)
    print(f"array b : {b} with shape : {b.shape}")
#reshape_array()

def math_ops():
    a = np.array([[1,2,3,4], [5,6,7,8],[9,10,11,12]])
    five_up = a[a>5]
    print(f"Greater than five : {five_up}")
    b = a[(a>5) & (a<10)]
    print(b)
    c = np.nonzero(a<5)   # get the indices where a<5, [row indices] and [column indices]
    print(f"Nonzero indices: {c}")
    for i in zip(c[0],c[1]):
        print(i)
    print(a[c])     #Print the elem less than 5

#math_ops()

'''This is why Nunpy is widely used for machine learning'''
def complex_math_ops():
    predictions = np.array([1,1,1])
    labels = np.array([1,2,3])
    # Formula : mean_square_error_formula = 1/n * np.sum(np.square(predictions - labels))
    mean_square_error = 1/3 * np.sum(np.square(predictions - labels))
    print(mean_square_error)
#complex_math_ops()

'''Saving and loading into files: 
While text files can be easier for sharing, .npy and .npz files are smaller and faster to read.'''
def load_save_to_file():
    a = np.array([1, 2, 3, 4, 5, 6])
    np.save('filename', a)  #You can save it as “filename.npy” with:
    b = np.load('filename.npy')
    print(b)

    np.savetxt("filename.csv", a)
    c = np.loadtxt("filename.csv")
    print(c)
load_save_to_file()

'''NumPy with Pandas'''
import pandas as pd
def num_pandas():
    a = np.array([
        [-2.58289208,  0.43014843, -1.24082018, 1.59572603],
        [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
        [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
        [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]
    ])
    
    df = pd.DataFrame(a)
    print(df)
    df.to_csv("pandas.csv")
    data = pd.read_csv("pandas.csv")
    print(data)

#num_pandas()

'''Plotting graphs w matplotlib'''
import matplotlib.pyplot as plt
def plot_graphs():
    a = np.array([1,2,5,10,3,90,42,7,5,3,4])
    plt.plot(a)
    #plt.show()     #This command shows graph from command line

#plot_graphs()