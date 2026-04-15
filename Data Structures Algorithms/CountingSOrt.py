'''Complexity = O(n+k)
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingElem(arr):
    # Write your code here
    max_index = max(arr) + 1    # +1 Since index starts from 0
    print(max_index)
    counting_list = [0] * max_index      #List of indexes [0, 0, 0, 0, 0, 0]
    #print(counting_list)
    for element in arr:
        #print(element)
        if(counting_list[element] == 0):
            #print("set index to 1")
            counting_list[element] = 1
        else:
            #print("Increment by 1")
            counting_list[element] = counting_list[element] + 1
    print(counting_list)
    return counting_list

def countingSort(count_arr):
    sorted_list = []
    #print(count_arr)
    for ind, val in enumerate(count_arr):
        #print(ind, val)
        for i in range(val):
            if(val != 0):
                sorted_list.append(ind)
            else:
                break
    #print(sorted_list)
        


if __name__ == '__main__':
   

    arr = [1, 1, 3, 2, 1]
    arr = [63,54,17,78,43,70,32,97,16,94,74,18,60,61,35,83,13,56,75,52,70,12,24,37,17,0,16,64,34,81,82,24,69,2,30,61,83,37,97,16,70,53,0,61,12,17,97,67,33,30,49,70,11,40,67,94,84,60,35,58,19,81,16,14,68,46,42,81,75,87,13,84,33,34,14,96,7,59,17,98,79,47,71,75,8,27,73,66,64,12,29,35,80,78,80,6,5,24,49,82]

    counting_list = countingElem(arr)
    sorted_elem = countingSort(counting_list)

    
