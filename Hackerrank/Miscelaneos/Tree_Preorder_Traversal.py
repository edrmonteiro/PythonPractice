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

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    queue = [root]
    output = ""
    while queue:
        node = queue.pop()
        output += str(node.info) + " " 
        while node.left or node.right:
            if node.left:
                if node.right:
                    queue.append(node.right)
                node = node.left
                output += str(node.info) + " "
            elif node.right:
                node = node.right
                output += str(node.info) + " " 

    # print(output)
    return output[:-1] 

tree = BinarySearchTree()
input_data = "1 14 3 7 4 5 15 6 13 10 11 2 12 8 9" #1 14 3 2 7 4 5 6 13 10 8 9 11 12 15 
input_split = input_data.split()
t = int(len(input_split))
arr = list(map(int,input_split))
for i in range(t):
    tree.create(arr[i])
print(preOrder(tree.root))

end = True