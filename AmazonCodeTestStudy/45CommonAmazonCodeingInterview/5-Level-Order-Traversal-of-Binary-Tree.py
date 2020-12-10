"""
5 - Level Order Traversal of Binary Tree
Problem Statement
Given the root of a binary tree, display the node values at each level. 
Node values for all levels should be displayed on separate lines. Let’s take a look at the below binary tree.

    100
    / \
   50  200
  / \   / \
25  75     350

Level order traversal for this tree should look like:

100
50, 200
25, 75, 350
"""
# Using two queues
from collections import defaultdict

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


    def display(self):
        elements = []
        queue = []
        node = self
        queue.append(node)

        while len(queue) > 0:
            node = queue.pop(0)
            elements.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(elements)

    def displayTransversal(self):
        elements = defaultdict(list)
        queue = []
        node = self
        queueTransversal = [1]
        queueTransversal.append(node)
        queue.append(queueTransversal)

        while len(queue) > 0:
            queueTransversal = queue.pop(0)
            level = queueTransversal.pop(0)
            while len(queueTransversal) > 0:
                node = queueTransversal.pop(0)
                elements[level].append(node.data)
                queueTNew = [level + 1]
                if node.left:
                    queueTNew.append(node.left)
                if node.right:
                    queueTNew.append(node.right)
                if len(queueTNew) > 1:
                    queue.append(queueTNew)

        print(len(elements))
        for i in range(len(elements)):
            print(elements[i + 1])
  
node = Node(100)
node.left = Node(50)
node.left.left = Node(25)
node.left.right = Node(75)
node.right = Node(200)
node.right.right = Node(350)
node.display()
node.displayTransversal()

stop = True


"""
Solution Explanation
Runtime Complexity
The runtime complexity of this solution is linear, O(n).

Memory Complexity
The memory complexity of this solution is linear, O(n).


Solution Breakdown
Here, you are using two queues: current_queue and next_queue. You push the nodes in both queues alternately based on the current level number.

You’ll dequeue nodes from the current_queue, print the node’s data, and enqueue the node’s children to the next_queue. Once the current_queue becomes empty, you have processed all nodes for the current level_number. To indicate the new level, print a line break (’\n’), swap the two queues, and continue with the above-mentioned logic.

After printing the leaf nodes from the current_queue, swap current_queue and next_queue. Since the current_queue would be empty, you can terminate the loop.
"""