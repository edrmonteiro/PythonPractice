"""
11. Find all subsets of a given set of integers
We are given a set of integers, and we have to find all the possible subsets of this set of integers. 
The following example elaborates on this further. 
"""

def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
      return 0
    return 1
        
def get_all_subsets(v, sets):
    subsets_count = 2 ** len(v)
    for i in range(0, subsets_count):
      st = set([])
      for j in range(0, len(v)):
         if get_bit(i, j) == 1:
            st.add(v[j])
      sets.append(st)
      
def main():
    v = [8,13,3,22,17,39,87,45,36]
    v = [1, 2, 3]
    subsets = []
    get_all_subsets(v, subsets);
    print("****Total*****" + str(len(subsets)))
    for i in range(0, len(subsets)):
        print("{", end = "")
        print(subsets[i], end = "")
        print("}")
    print("****Total*****" + str(len(subsets)))
 
main()

stop = True


"""
Runtime Complexity: Exponential, O(2^n∗n)
Memory Complexity: Exponential, O(2^n∗n)
There are several ways to solve this problem. We will discuss the one that is neat and easier to understand. We know that for a set of n elements there are 2^n subsets. For example, a set with three elements will have eight subsets. Here is the algorithm we will use:
n = size of given integer set
subsets_count = 2^n
for i = 0 to subsets_count
    form a subset using the value of 'i' as following:
        bits in number 'i' represent index of elements to choose from original set,
        if a specific bit is 1 choose that number from original set and add it to current subset,
        e.g. if i = 6 i.e 110 in binary means that 1st and 2nd elements in original array need to be picked.
    add current subset to list of all subsets
"""