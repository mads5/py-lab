'''
#Iterator methods implementation
class ArrayIterator:
    def __init__(self, arr):
        self.arr = arr
    
    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if(self.pos < len(self.arr)):
            self.pos = self.pos + 1
            return self.arr[self.pos - 1]
        else:
            raise StopIteration

o = ArrayIterator([1,2,3])
it = o.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
#print(it.__next__())
'''
###Generator
def reverse(li):
    for i in range(len(li)-1, -1, -1):
        yield li[i]

for char in reverse('golf'):
    print(char)