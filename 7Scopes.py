"""The global statement can be used to indicate that particular variables live in the global scope and that value is accessible from there; 
the nonlocal statement indicates that particular variables live in an enclosing scope and that value should be accessible from there."""

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam 
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    print(f"spam value before scope call : {spam}")
    do_local()
    print(f"spam value after local call : {spam}")
    do_nonlocal()
    print(f"spam value after nonlocal call : {spam}")
    #do_global()
    print(f"spam value after global call : {spam}")


scope_test()
print(f"spam value after scopetest function global level : {spam}")

"""Conclusion : Local assignment (which is default) didn’t change scope_test's binding of spam
 The nonlocal assignment changed scope_test's binding of spam
 the global assignment changed the module-level binding. You can also see that there was no previous binding for spam before the global assignment."""
