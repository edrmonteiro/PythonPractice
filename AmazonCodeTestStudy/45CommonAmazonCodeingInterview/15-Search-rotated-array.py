"""
15. Search rotated array
Search for a given number in a sorted array, with unique elements, that has been rotated by some arbitrary number. 
Return -1 if the number does not exist. Assume that the array does not contain duplicates. 
"""
def binary_search(arr, start, end, key):
  # assuming all the keys are unique.
  
  if (start > end):
    return -1
 
  mid = int(start + (end - start) / 2)
 
  if arr[mid] == key:
    return mid
    
  if arr[start] <= arr[mid] and key <= arr[mid] and key >= arr[start]:
    return binary_search(arr, start, mid - 1, key)
  
  elif arr[mid] <= arr[end] and key >= arr[mid] and key <= arr[end]: 
    return binary_search(arr, mid + 1, end, key)

array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
key = 5
index = binary_search(array, 0, len(array) - 1, key)
print("Index:" + str(index))


stop = True

"""
Runtime Complexity: Logarithmic, O(logn)
Memory Complexity: Logarithmic, O(logn)
The solution is essentially a binary search but with some modifications. 
If we look at the array in the example closely, we notice that at least one-half of the array is always sorted. 
We can use this property to our advantage. 
If the number n lies within the sorted half of the array, then our problem is a basic binary search. 
Otherwise, discard the sorted half and keep examining the unsorted half. 
Since we are partitioning the array in half at each step, this gives us O(logn)O(logn) runtime complexity.


"""