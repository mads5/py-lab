'''The design of singly-linked lists makes them a useful data structure when performing operations that occur 
at the beginning of the list with time complexity of O(1).
However, insertion and deletion in the middle or at the end requires traversing the list until that point, 
leading to an O(n) time complexity.
Node : Data + Next Pointer, started at Head
'''
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.nextval = None     #This will be updated to next node while doing operations

class SLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertAtEnd(self, data) -> None:
        if self.head is None:
            self.insertAtBeginnning(data)
        newNode = Node(data)
        current = self.head
        while current.nextval is not None:
            current = current.nextval
        current.nextval = newNode

    def deleteFromBeginning(self) -> None:
        current = self.head
        self.head.nextval = self.head
        

class SLinkedList:
    def __init__(self) -> None:
        self.head = None        
        #self.head will always point to the Node and will have node attributes like 'data' and 'nextval'

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.nextval = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        if self.head is None:
            self.insertAtBeginning(data)
            return
        
        new_node = Node(data)
        current_node = self.head

        while current_node.nextval:
            current_node = current_node.nextval
        current_node.nextval = new_node

    def checkEmptyList(self):
        if self.head is None:
            return "List is empty"

    def deleteFromBeginning(self):
        self.checkEmptyList()
        self.head = self.head.nextval

    def deleteFromEnd(self):
        self.checkEmptyList()
        
        if self.head.nextval is None:  # There is only 1 node after head
            self.head = None
        
        current_node = self.head
        while current_node.nextval.nextval:     #Checking current_node with one next two node values
            current_node = current_node.nextval
        current_node.nextval = None     #second last node becomes the last node

    def insertAtIndex(self, data, index):
        if(index == 0):
            self.insertAtBeginning(data)
        
        current_node = self.head
        position = 0
        while(current_node and position+1 != index):
            position = position + 1
            current_node = current_node.nextval
        if(current_node is not None):
            new_node = Node(data)
            new_node.nextval = current_node.nextval
            current_node.nextval = new_node
        else:
            print(f"Index {index} is not present in List")

    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.nextval    #Track next node
            current_node.nextval = prev_node    #Modify current node

            prev_node = current_node        #Update prev and current
            current_node = next_node
        self.head = prev_node

    def searchValue(self, data):
        current_node = self.head
        index = 0
        while current_node:
            if(current_node.data == data):
                print(f"Data {data} found at index {index}")
                return
            current_node = current_node.nextval
            index = index + 1
        else:
            print(f"Data '{data}' is not present in Linked list")

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.nextval
        print("\n")

    def sizeLL(self):
        temp = self.head
        size = 0
        while temp:
            size = size + 1
            temp = temp.nextval
        print(f"Current Size of LL is : {size}")
    
    def merge_ll(self, l1, l2):
        l2_current = l2.head
        # traverse any one LL
        while l1.head:
            if(l1.head.data <= l2_current.data):
                l1_current = l1.head
                l1.head = l1.head.nextval
                l1_current.nextval = l2_current
            elif(l1.head.data > l2_current.data):
                while(l2_current):
                    if(l1.head.data > l2_current.data):
                        l2_current = l2_current.nextval
                    else:
                        pass
        # Compare values one by one with another LL
        # And add references based on sort comparison


object_ll = SLinkedList()
#print(object_ll)

# Insert new node at beginning
object_ll.insertAtBeginning('on')
object_ll.insertAtBeginning('Wheels')
#object_ll.printLL()

object_ll.insertAtEnd('the')
object_ll.insertAtEnd('bus')
object_ll.printLL()
object_ll.sizeLL()

object_ll.insertAtIndex('Round', 2)
object_ll.printLL()

object_ll.searchValue('bus')
object_ll.searchValue('and')

object_ll.reverse()
object_ll.printLL()
''' Deleting a node
object_ll.deleteFromBeginning()
object_ll.printLL()
object_ll.deleteFromEnd()
object_ll.printLL()
'''


# Merge two sorted linked list in sorted manner
#If the first list is: 1 -> 4 -> 5 -> NULL and the second list is: 2 -> 3 -> 5 -> NULL 
# The final list would be: 1 -> 2 -> 3 -> 4 -> 5 -> 5 -> NULL
print("-----Merging two sorted lists-------")
object_l1 = SLinkedList()
object_l1.insertAtBeginning(1)
object_l1.insertAtEnd(2)
object_l1.insertAtEnd(3)
object_l1.printLL()

object_l2 = SLinkedList()
object_l2.insertAtBeginning(1)
object_l2.insertAtEnd(3)
object_l2.printLL()

x = SLinkedList()
x.merge_ll(object_l1, object_l2)
