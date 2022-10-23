"""
707. Design Linked List
Medium

1850

1321

Add to List

Share
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
class MyLinkedList:
    def __init__(self):
        self.val = None
        self.next = None
        
    def get(self, index: int) -> int:
        node = self
        for i in range(index):
            if node.next:
                node = node.next
            else:
                return -1
        if node.val == None:
            return -1
        return node.val
            
    def addAtHead(self, val: int) -> None:
        if self.val or self.val == 0:
            node = MyLinkedList()
            node.next = self.next
            node.val = self.val
            self.val = val
            self.next = node
        else:
            self.val = val

    def addAtTail(self, val: int) -> None:
        if self.val == None:
            self.val = val
        else:
            node = self
            while node.next:
                node = node.next
            node.next = MyLinkedList()
            node = node.next
            node.val = val

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        node = self
        for i in range(index-1):
            if node.next:
                node = node.next
            else:
                return 
        tail = node.next
        new = MyLinkedList()
        new.val = val
        new.next = tail
        node.next = new

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            node = self
            if node.next:
                node = node.next
                self.val = node.val
                self.next = node.next
            else:
                self.val =  None
                self.next = None
            return
        node = self
        for i in range(index-1):
            if node.next:
                node = node.next
            else:
                return 
        if node.next and node.next.next:
            node.next = node.next.next
        else:
            node.next = None
        
        
# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# print(obj.get(1))
# obj.deleteAtIndex(1)
# print(obj.get(1))

# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.deleteAtIndex(0)
# print(obj.get(1))
# param_1 = obj.get(1)

# methods = ["MyLinkedList","addAtHead","addAtTail","addAtHead","addAtTail","addAtHead","addAtHead","get","addAtHead","get","get","addAtTail"]
# itens = [[],[7],[7],[9],[8],[6],[0],[5],[0],[2],[5],[4]]

# obj = MyLinkedList()
# obj.addAtHead(7)    
# obj.addAtTail(7)
# obj.addAtHead(9)
# obj.addAtTail(8)
# obj.addAtHead(6)
# obj.addAtHead(0)
# print(obj.get(5))
# obj.addAtHead(0)
# print(obj.get(2))
# print(obj.get(5))
# obj.addAtTail(4)
# obj.addAtTail()

# obj = MyLinkedList()
# obj.addAtTail(1)
# print(obj.get(0))

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))
print(obj.get(3))
obj.deleteAtIndex(3)
obj.deleteAtIndex(0)
print(obj.get(0))
obj.deleteAtIndex(0)
print(obj.get(0))

param_1 = obj.get(1)
