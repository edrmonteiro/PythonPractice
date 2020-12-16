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