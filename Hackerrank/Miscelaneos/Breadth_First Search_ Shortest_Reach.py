#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
class Node():
    def __init__(self,data):
        self.data = data
        self.edges = []

def bfs(n, m, edges, s):
    # Write your code here
    #create the nodes
    node_list = []
    for i in range(n):
        node_list.append(Node(i+1))
    
    #insert edges
    for edge in edges:
        node_list[edge[0]-1].edges.append(node_list[edge[1]-1])
        node_list[edge[1]-1].edges.append(node_list[edge[0]-1])

    paths = [-1]*n
    queue = [[node_list[s-1],0]]
    nodes_visited = [s]
    while queue:
        node, depth = queue.pop(0)
        depth += 6
        print(node.data)
        for edge in node.edges:
            print(edge.data)
            paths[edge.data-1] = depth if paths[edge.data-1] == -1 else min(paths[edge.data-1],depth)
            if edge.data not in nodes_visited:
                nodes_visited.append(edge.data)
                queue.append([edge,depth])

    paths.pop(s-1)
    return paths

# n = 4
# m = 2
# edges = [[1,2],[1,3]]
# s = 1 # 6 6 -1
# print(bfs(n, m, edges, s))

# n = 3
# m = 1
# edges = [[2,3]]
# s = 2 # -1 6
# print(bfs(n, m, edges, s))

n = 5 
m = 3 
edges = [[1, 2], [1, 3], [3, 4]] 
s= 1
print(bfs(n, m, edges, s))
#exp[ected] 6 6 12 -1
#minha 6 6 6 -1

n = 10 
m = 6 
edges = [[3, 1], [10, 1], [10, 1], [3, 1], [1, 8], [5, 2]] 
s = 3
#errado  6 -1 -1 -1 -1 -1 6 -1 6
print(bfs(n, m, edges, s))
# 6 6 12 -1


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         edges = []

#         for _ in range(m):
#             edges.append(list(map(int, input().rstrip().split())))

#         s = int(input().strip())

#         result = bfs(n, m, edges, s)

#         fptr.write(' '.join(map(str, result)))
#         fptr.write('\n')

#     fptr.close()
