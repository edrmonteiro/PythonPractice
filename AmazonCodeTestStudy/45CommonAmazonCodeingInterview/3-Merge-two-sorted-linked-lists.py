"""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted. 
Consider two sorted linked lists and the merged list below them as an example. Click here to view the solution in C++, Java, JavaScript, and Ruby.
head1 -> 4 -> 8 -> 15 -> 19 -> null
head2 -> 7 -> 9 -> 10 -> 16 -> null

head1 -> 4 -> 7 -> 8 -> 9-> 10 -> 15 -> 16 -> 19 -> NULL
"""
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def insert(self, A):
        node = self
        for data in A:
            node.next = Node(data)
            node = node.next

    def display(self):
        elements = []
        node = self
        while True:
            elements.append(node.data)
            if node.next:
                node = node.next
            else:
                break        
        print(elements)

    def get(self, index):
        if index >= self.length():
            print ("ERROR: 'Get' index out of range!")
            return None
        currentIndex = 0
        currentNode = self.head
        while True:
            currentNode = currentNode.next
            if currentIndex == index: return currentNode.data
            currentIndex += 1

    def erase(self, index):
        if index >= self.length():
            print ("ERROR: 'Erase' Index out of range!")
            return
        currentIndex = 0
        currentNode = self.head
        while True:
            lastNode = currentNode
            currentNode = currentNode.next
            if currentIndex == index:
                lastNode.next = currentNode.next
                return
            currentIndex += 1

def merge_sorted(head1, head2):
  # if both lists are empty then merged list is also empty
  # if one of the lists is empty then other is the merged list
  if head1 == None:
    return head2
  elif head2 == None:
    return head1

  mergedHead = None
  if head1.data <= head2.data:
    mergedHead = head1
    head1 = head1.next
  else:
    mergedHead = head2
    head2 = head2.next

  mergedTail = mergedHead
  
  while head1 != None and head2 != None:
    temp = None
    if head1.data <= head2.data:
      temp = head1
      head1 = head1.next
    else:
      temp = head2
      head2 = head2.next

    mergedTail.next = temp
    mergedTail = temp

  if head1 != None:
    mergedTail.next = head1
  elif head2 != None:
    mergedTail.next = head2

  return mergedHead

def create_linked_list(A):    
    node = Node(A[0])
    A = A[1:]
    node.insert(A)
    return node

array1 = [2, 3, 5, 6]
linkedList1 = create_linked_list(array1)
print("Original1:")
linkedList1.display()

array2 = [1, 4, 10]
linkedList2 = create_linked_list(array2)
print("\nOriginal2:")
linkedList2.display()

new_head = merge_sorted(linkedList1, linkedList2)
print("\nMerged:")
new_head.display()

stop = True



"""
Runtime Complexity: Linear, O(m+n) where m and n are lengths of both linked lists
Memory Complexity: Constant, O(1)
Maintain a head and a tail pointer on the merged linked list. 
Then choose the head of the merged linked list by comparing the first node of both linked lists. 
For all subsequent nodes in both lists, you choose the smaller current node, link it to the tail of the merged list, 
and move the current pointer of that list one step forward.
Continue this while there are some remaining elements in both the lists. If there are still some elements in only one of the lists, 
you link this remaining list to the tail of the merged list. Initially, the merged linked list is NULL.
Compare the value of the first two nodes and make the node with the smaller value the head node of the merged linked list. 
In this example, it is 4 from head1. Since it’s the first and only node in the merged list, it will also be the tail. Then move head1 one step forward.
"""