"""
4. Copy linked list with arbitrary pointer
You are given a linked list where the node has two pointers. 
The first is the regular next pointer. 
The second pointer is called arbitrary_pointer, and it can point to any node in the linked list. 
Your job is to write code to make a deep copy of the given linked list. 
Here, deep copy means that any operations on the original list should not affect the copied list.
7 -> 14 -> 21 -> Null

https://www.geeksforgeeks.org/clone-linked-list-next-random-pointer-o1-space/
"""

'''Python program to clone a linked list with next and arbitrary pointers'''
'''Done in O(n) time with O(1) extra space'''
  
class Node: 
    '''Structure of linked list node'''
  
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.random = None
  
def clone(original_root): 
    '''Clone a doubly linked list with random pointer'''
    '''with O(1) extra space'''
  
    '''Insert additional node after every node of original list'''
    curr = original_root 
    while curr != None: 
        new = Node(curr.data) 
        new.next = curr.next
        curr.next = new 
        curr = curr.next.next
  
    '''Adjust the random pointers of the newly added nodes'''
    curr = original_root 
    while curr != None: 
        curr.next.random = curr.random.next
        curr = curr.next.next
  
    '''Detach original and duplicate list from each other'''
    curr = original_root 
    dup_root = original_root.next
    while curr.next != None: 
        tmp = curr.next
        curr.next = curr.next.next
        curr = tmp 
  
    return dup_root 
  
def print_dlist(root): 
    '''Function to print the doubly linked list'''
  
    curr = root 
    while curr != None: 
        print('Data =', curr.data, ', Random =', curr.random.data) 
        curr = curr.next
  
####### Driver code ####### 
'''Create a doubly linked list'''
original_list = Node(1) 
original_list.next = Node(2) 
original_list.next.next = Node(3) 
original_list.next.next.next = Node(4) 
original_list.next.next.next.next = Node(5) 
  
'''Set the random pointers'''
  
# 1's random points to 3 
original_list.random = original_list.next.next
  
# 2's random points to 1 
original_list.next.random = original_list 
  
# 3's random points to 5 
original_list.next.next.random = original_list.next.next.next.next
  
# 4's random points to 5 
original_list.next.next.next.random = original_list.next.next.next.next
  
# 5's random points to 2 
original_list.next.next.next.next.random = original_list.next
  
'''Print the original linked list'''
print('Original list:') 
print_dlist(original_list) 
  
'''Create a duplicate linked list'''
cloned_list = clone(original_list) 
  
'''Print the duplicate linked list'''
print('\nCloned list:') 
print_dlist(cloned_list) 
  
'''This code is contributed by Shashank Singh'''

stop = True

"""
Runtime Complexity: Linear, O(n)
Memory Complexity: Linear, O(n)
This approach uses a map to track arbitrary nodes pointed by the original list. 
You will create a deep copy of the original linked list (say list_orig) in two passes.
In the first pass, create a copy of the original linked list. While creating this copy, 
use the same values for data and arbitrary_pointer in the new list. 
Also, keep updating the map with entries where the key is the address to the old node and the value is the address of the new node.
Once the copy has been created, 
do another pass on the copied linked list and update arbitrary pointers to the new address using the map created in the first pass.
"""
