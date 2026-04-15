# Enter your code here. Read input from STDIN. Print output to STDOUT
def queue_functions(func, q, n = 0):
    if(int(func) == 1):
        #Enqueue
        q.append(n)
    elif(int(func) == 2):
        #Dequeue
        q.pop(0)
    elif(int(func) == 3):
        print(str(q[0]))
    else:
        print("Invalid function input provided")
    
    return q

if __name__ == "__main__":
    queue = []
    #Collect input
    queries = int(input())

    for function in range(queries):
        input_str = input()
        #print(input_str)
        if(input_str.__contains__(" ")):
            #print("Enqueue")
            process, num = str(input_str).split(" ")
            queue = queue_functions(process, queue, num)
        else:
            #print("Dequeue or print")
            process = str(input_str)
            queue = queue_functions(process, queue)

"""
Sample Input
------------
STDIN   Function
-----   --------
10      q = 10 (number of queries)
1 42    1st query, enqueue 42
2       dequeue front element
1 14    enqueue 42
3       print the front element
1 28    enqueue 28
3       print the front element
1 60    enqueue 60
1 78    enqueue 78
2       dequeue front element
2       dequeue front element

Sample Output
-------------
14
14
"""