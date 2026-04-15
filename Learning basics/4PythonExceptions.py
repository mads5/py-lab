try:
    x = int(input("Please enter an integer"))
    #raise Exception("spam", "eggs")
except Exception as e:
    print(type(e))
    print(f"Args of exception : {e.args}")
    print(f"Exception object e : {e}")

    #Unpacking in case of raising exception of line 3
    #x, y = e.args
    #print(f"x : {x} and y : {y}")
else:   # Else is excuted in case no execptions have been raised
    print("The code did not raise any exception")
finally:    #If the finally clause executes a break, continue or return statement, exceptions are not re-raised
    print("This will always run even if exception is raised or not")
    #the finally clause is useful for releasing external resources (such as files or network connections),
    
"""BaseException is the common base class of all exceptions.
One of its subclasses, Exception, is the base class of all the non-fatal exceptions.
Exceptions which are not subclasses of Exception indicate that the program should exit : 'SystemExit' which is 
raised by sys.exit() and 'KeyboardInterrupt' which is raised when a user wishes to interrupt the program.
The most common pattern for handling Exception is to print or log the exception and then re-raise it"""
