# This is based on Divide and conquer algorithm.
# Divide the main unsorted array into smaller array based on pivot recursively until you get the sorted array
# Time complexity is O(n log n)
#The space complexity of the algorithm is O(n)

def quick_sort(arr):
    if(len(arr) <= 1):
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[0:] if x < pivot]
    right = [y for y in arr[0:] if y > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [5, 3, 6, 1, 10]
#arr = [1]
sorted_arr = quick_sort(arr)
print(sorted_arr)