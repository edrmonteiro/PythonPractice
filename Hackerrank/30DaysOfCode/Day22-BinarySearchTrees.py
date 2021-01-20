"""
Hackerrank
Day 22: Binary Search Trees
https://www.hackerrank.com/challenges/30-binary-search-trees/problem?h_r=email&unlock_token=5536f1c3d2f132073ddfd79b768a8921df47ce60&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
Objective
Today, we're working with Binary Search Trees (BSTs). Check out the Tutorial tab for learning materials and an instructional video!

Task
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, , pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a binary search tree:
The first line contains an integer, , denoting the number of nodes in the tree.
Each of the  subsequent lines contains an integer, , denoting the value of an element that must be added to the BST.

Output Format

The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

Sample Input

7
3
5
2
1
4
6
7
Sample Output

3
Explanation

The input forms the following BST:

BST.png

The longest root-to-leaf path is shown below:

Longest RTL.png

There are  nodes in this path that are connected by  edges, meaning our BST's . Thus, we print  as our answer.

"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    
    def getHeightLevel(self, root, height):
        if not root.left and not root.right: 
            return height
        if root.left and root.right:
            return max(self.getHeightLevel(root.left, height + 1), self.getHeightLevel(root.right, height + 1))
        if root.left:
            return self.getHeightLevel(root.left, height + 1)
        if root.right:
            return  self.getHeightLevel(root.right, height + 1)
            
    def getHeight(self,root):
        #Write your code here
        return self.getHeightLevel(root, 0)
     
            
# T=int(input())
# myTree=Solution()
# root=None
# for i in range(T):
#     data=int(input())
#     root=myTree.insert(root,data)
# height=myTree.getHeight(root)
# print(height)

#T=int(input())
myTree=Solution()
root=None
T = [3, 5, 2, 1, 4, 6, 7]
#T = [20, 50, 35, 44, 9, 15, 62, 11, 13]
for data in T:
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
stop = True

