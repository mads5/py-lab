"""Pre-requisites : Data to be searched needs to be sorted"""
'''The iterative method)(Preferred) of binary search has a time complexity of O(log n) because the search interval
is halved with each iteration. Its space complexity is O(1) since it uses a constant amount of extra space'''
'''The recursive method also has a time complexity of O(log n) for the same reason. However, its space 
complexity is O(log n) due to the space needed to maintain the call stack for each recursive call'''

def find_target_w_binaryS(array, target_val):
    left = 0
    right = len(array) - 1
    while(left <= right):
        middle_index = (left + right) // 2
        print(middle_index)
        if(array[middle_index] == target_val):
            return middle_index
        elif(array[middle_index] < target_val):
            left = middle_index + 1
        else:
            right = middle_index - 1
    else :
        return -1


li1 = [4,1,6,3,15,7,2]
li1 = sorted(li1)
print(li1)

result = find_target_w_binaryS(li1, 15)
if result!= -1:
    print(f"Target value is found at index {result}")
else:
    print(f"Target value is not present in the list")

#from jovian.pythondsa import evaluate_test_case
#tests = [{'input':{li1, 15}, 'output' : 12}]
#evaluate_test_case(find_target_w_binaryS, tests)
'''Test scenarios including edge cases (List is reverse in this case):
[{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
  'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
   'query': 6},
  'output': 2}]
'''