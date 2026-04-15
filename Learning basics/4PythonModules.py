"""This will import all names except the ones which start with '_' """
from sys import *

li1 = [1,2,3]
"""If the module name is followed by as, then the name following as is bound directly to the imported module.
This can be also used with 'from' """
import sys as sys1
sys1.getsizeof(li1)

if __name__== "__main__":
    print("You are Running the current module as script")

print(sys1.path)

# This will generate a compiled copy of the PythonVariables module in __pycache__ directory.
import PythonVariables

print(f"dir function on list variable : {dir(li1)}")
print(f"dir function on PythonVariables module : {dir(PythonVariables)}")



"""Importing a user defined package 'package1' """
import os
import sys
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
print(f"current Script path : {SCRIPT_PATH}")
sys.path.append(os.path.dirname(SCRIPT_PATH))
# Added the path explicitely to the sys.path/PYTHONPATH
from package1 import effects