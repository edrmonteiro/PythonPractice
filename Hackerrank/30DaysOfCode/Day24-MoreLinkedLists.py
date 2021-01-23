"""
Hackerrank
Day 24: More Linked Lists
https://www.hackerrank.com/challenges/30-linked-list-deletion/problem?h_r=email&unlock_token=c00eb8517bdf68ed276f8d6f8884a978fc64bb14&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
Objective
Check out the Tutorial tab for learning materials and an instructional video!

Task
A Node class is provided for you in the editor. A Node object has an integer data field, , and a Node instance pointer, , pointing to another node (i.e.: the next node in a list).

A removeDuplicates function is declared in your editor, which takes a pointer to the  node of a linked list as a parameter. Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.

Note: The  pointer may be null, indicating that the list is empty. Be sure to reset your  pointer when performing deletions to avoid breaking the list.

Input Format

You do not need to read any input from stdin. The following input is handled by the locked stub code and passed to the removeDuplicates function:
The first line contains an integer, , the number of nodes to be inserted.
The  subsequent lines each contain an integer describing the  value of a node being inserted at the list's tail.

Constraints

The data elements of the linked list argument will always be in non-decreasing order.
Output Format

Your removeDuplicates function should return the head of the updated linked list. The locked stub code in your editor will print the returned list to stdout.

Sample Input

6
1
2
2
3
3
4
Sample Output

1 2 3 4 
Explanation

, and our non-decreasing list is . The values  and  both occur twice in the list, so we remove the two duplicate nodes. We then return our updated (ascending) list, which is 

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        numbers = []
        node = head
        previous = None
        while node:            
            if node.data not in numbers:
                numbers.append(node.data)
                previous = node                          
            else:
                if node.next:
                    previous.next = node.next
                else:
                    previous.next = None
            node = node.next  
        return head
                

# mylist= Solution()
# T=int(input())
# head=None
# for i in range(T):
#     data=int(input())
#     head=mylist.insert(head,data)    
# head=mylist.removeDuplicates(head)
# mylist.display(head); 

mylist= Solution()
head=None
A = [1, 1, 1, 1, 1, 1, 1]
#A = [1,2,2,3,3,4]
for data in A:
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 

stop = True
