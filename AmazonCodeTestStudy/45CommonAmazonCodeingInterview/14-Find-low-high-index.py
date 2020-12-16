"""
14. Find low/high index
Given a sorted array of integers, return the low and high index of the given key. You must return -1 if the indexes are not found. The array length can be in the millions, with many duplicates.
In the following example, according to the key, the low and high indices would be:
key: 1, low = 0 and high = 0
key: 2, low = 1 and high = 1
key: 5, low = 2 and high = 9
key: 20, low = 10 and high = 10

For the testing of your code, the input array will be:
1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6
"""

def find_low_index(arr, key):
  low = 0
  high = len(arr) - 1
  mid = int(high / 2)
 
  while low <= high:
    mid_elem = arr[mid]
    if mid_elem < key:
      low = mid + 1
    else:
      high = mid - 1
    mid = low + int((high - low) / 2)

  if low < len(arr) and arr[low] == key:
    return low
 
  return -1
 
def find_high_index(arr, key):
  low = 0
  high = len(arr) - 1
  mid = int(high / 2)

  while low <= high:
    mid_elem = arr[mid]
    if mid_elem <= key:
      low = mid + 1
    else:
      high = mid - 1
    mid = low + int((high - low) / 2)
  
  if high == -1:
    return high
 
  if high < len(arr) and arr[high] == key:
    return high
 
  return -1
 
 
array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
key = 5
low = find_low_index(array, key)
high = find_high_index(array, key)
print("Low Index of " + str(key) + ": " + str(low))
print("High Index of " + str(key) + ": " + str(high))
 
key = -2
low = find_low_index(array, key)
high = find_high_index(array, key)
print("Low Index of " + str(key) + ": " + str(low))
print("High Index of " + str(key) + ": " + str(high))

stop = True


"""
Runtime Complexity: Logarithmic, O(logn)
Memory Complexity: Constant, O(1)
Linearly scanning the sorted array for low and high indices is highly inefficient since our array size can be in millions. 
Instead, we will use a slightly modified binary search to find the low and high indices of a given key. 
We need to do binary search twice: once for finding the low index, once for finding the high index.
Let’s look at the algorithm for finding the low index. 
At every step, consider the array between low and high indices and calculate the mid index.
If the element at mid index is less than the key, lowbecomes mid + 1 (to move towards the start of range).
If the element at mid is greater or equal to the key, the high becomes mid - 1. Index at low remains the same.
When low is greater than high, low would be pointing to the first occurrence of the key.
If the element at low does not match the key, return -1.
Similarly, we can find the high index by slightly modifying the above condition:
Switch the low index to mid + 1 when element at mid index is less than or equal to the key.
Switch the high index to mid - 1 when the element at midis greater than the key.
"""