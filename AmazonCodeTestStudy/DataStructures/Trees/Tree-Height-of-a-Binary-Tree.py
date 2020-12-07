"""
coding: utf-8
Created on 03/12/2020

@author: github.com/edrmonteiro
From: Hackerrank challenges
Language: Python
Title: Tree: Height of a Binary Tree

The height of a binary tree is the number of edges between the tree's root and its furthest leaf. For example, the following binary tree is of height :

image
Function Description

Complete the getHeight or height function in the editor. It must return the height of a binary tree as an integer.

getHeight or height has the following parameter(s):

root: a reference to the root of a binary tree.
Note -The Height of binary tree with single node is taken as zero.

Input Format

The first line contains an integer , the number of nodes in the tree.
Next line contains  space separated integer where th integer denotes node[i].data.

Note: Node values are inserted into a binary search tree before a reference to the tree's root node is passed to your function. In a binary search tree, all nodes on the left branch of a node are less than the node value. All values on the right branch are greater than the node value.

Constraints



Output Format

Your function should return a single integer denoting the height of the binary tree.

Sample Input

image

Sample Output

3
Explanation

The longest root-to-leaf path is shown below:

image

There are  nodes in this path that are connected by  edges, meaning our binary tree's .


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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    leftHeight = 0
    rightHeight = 0
    print(root)
    
    if root.left:
        leftHeight = 1 + height(root.left)
    if root.right:
        rightHeight = 1 + height(root.right)
    
    return leftHeight if leftHeight > rightHeight else rightHeight


root = Node(3) 

node2 = Node(2) 
root.left = node2 
node1 = Node(1) 
node2.left = node1 


node5 = Node(5)
root.right = node5
node4 = Node(4)
node5.left = node4

node6 = Node(6)
node5.right = node6
node7 = Node(7)
node6.right = node7

print(height(root))



root = Node(3) 
root.left = Node(2) 
root.left.left = Node(1)

root.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(6)
root.right.right.right = Node(7)

print(height(root))


stop = True





