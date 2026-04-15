
def file_op1():
    with open(r"C:\Users\skalantri\Desktop\python_prep\prep\Comprehensions.py",'r') as f:
        for line in f:
            print(line)
    print(f.closed)
#file_op1()

def file_op2():
    """f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode 
    and an opaque number when in text mode."""
    """To change the file object’s position, use f.seek(offset, whence). A whence value of 0 measures from the beginning of the file, 1 uses the current file position, 
    and 2 uses the end of the file as the reference point."""
    with open(r"C:\Users\skalantri\Desktop\python_prep\prep\file_out.txt", 'r+') as fw:
        fw.write("Hello and welcome to Bangalore")
        print(fw.tell())
        fw.seek(20)
        print(fw.read())

#file_op2()

def file_op3():
    f = open(r'C:\Users\skalantri\Desktop\python_prep\prep\file_out.txt', 'rb+')
    f.write(b'0123456789abcdef')
    print(f"Seek at 5 : {f.seek(5)}")      # Go to the 6th byte in the file
    print(f.read(1))
    print(f" Seek at -3,2 : {f.seek(-3, 2)}")  # Go to the 3rd byte before the end 
    print(f.read(1))

#file_op3()

import json
def file_json_op():
    x = '''{"one" : ["1", "Apple", ("x","y")]}'''
    fh = open(r"C:\Users\skalantri\Desktop\python_prep\prep\file_out.txt", "r+")
    json.dump(x, fh)

    json_str = '[{"name": "Alice", "age": 30}]'
    y = json.loads(json_str)
    print(y)

#file_json_op()

def file_op5():
    count = 0
    for row in open(r"C:\Users\skalantri\Desktop\python_prep\prep\Comprehensions.py",'r'):
        count = count + 1
        yield row
    print(count)

rows = file_op5()
next(rows)
next(rows)
