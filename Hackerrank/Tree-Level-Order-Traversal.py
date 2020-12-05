"""
Tree: Level Order Traversal
Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. 
In level-order traversal, nodes are visited level by level from left to right. 
Complete the function  and print the values in a single line separated by a space.

For example:

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
For the above tree, the level order traversal is .

Input Format

You are given a function,

void levelOrder(Node * root) {

}
Constraints

 Nodes in the tree  

Output Format

Print the values in a single line separated by a space.

Sample Input

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
Sample Output

1 2 5 3 6 4

Explanation

We need to print the nodes level by level. We process each level from left to right.
Level Order Traversal: .


"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def levelOrder(root):
     if not root:
          return
     queue = list()
     queue.append(root)
     nodes = '' 
     while len(queue) > 0:
          current = queue.pop(0)
          if current.left:
               queue.append(current.left)
          if current.right:
               queue.append(current.right)
          nodes += str(current.info) + ' '

     return nodes






root = Node(1) 
root.right = Node(2) 
root.right.right = Node(5)
root.right.right.right = Node(6)
root.right.right.left = Node(3)
root.right.right.left.right = Node(4)

print(levelOrder(root))


stop = True