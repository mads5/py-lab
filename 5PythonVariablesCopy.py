import copy
class PythonVariables:
    x = [1, 4, [100, 200]]
    print(x)

    y = copy.copy(x)
    y[2][0] = 90
    print(x + y)

    z = copy.deepcopy(x)
    z[1] = 30
    print(x + z)

    print(f"ID of x : {id(x)}")
    print(f"ID of y : {id(y)}")
    print(f"ID of z : {id(z)}")


    # Using id(), we can determine if the variables points to the same object or not
    # The difference between shallow and deep copying is only relevant for compound objects 
    # (objects that contain other objects, like lists or class instances
    def check_ref_equality(a, b):
        if(id(a) == id(b)):
            print(f"The two variables with ids {id(a)} and {id(b)} points to the same object")
        else:
            print(f"The two variables with ids {id(a)} and {id(b)} have different references")


    check_ref_equality(x, y)
    #check_ref_equality(x, z)
