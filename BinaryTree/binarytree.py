"""
coding: utf-8
Created on 03/12/2020

@author: github.com/edrmonteiro
From: www.geeksforgeeks.org
Language: Python
Title: binarytree-module-in-python


"""

#from binarytree import Node
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



root = Node(3) 
root.left = Node(6) 
root.right = Node(8) 
  
# Getting binary tree 
print('Binary tree :', root) 
  
# Getting list of nodes 
print('List of nodes :', list(root)) 
  
# Getting inorder of nodes 
print('Inorder of nodes :', root.inorder) 
  
# Checking tree properties 
print('Size of tree :', root.size) 
print('Height of tree :', root.height) 
  
# Get all properties at once 
print('Properties of tree : \n', root.properties) 

stop = True