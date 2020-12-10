"""
BFS: Shortest Reach in a Graph
https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

Consider an undirected graph consisting of  nodes where each node is labeled from  to  and the edge between any two nodes is always of length . We define node  to be the starting position for a BFS. Given a graph, determine the distances from the start node to each of its descendants and return the list in node number order, ascending. If a node is disconnected, it's distance should be .

For example, there are  nodes in the graph with a starting node . The list of , and each has a weight of .

Starting from node  and creating a list of distances, for nodes  through  we have .

Function Description

Define a Graph class with the required methods to return a list of distances.

Input Format

The first line contains an integer, , the number of queries.

Each of the following  sets of lines is as follows:

The first line contains two space-separated integers,  and , the number of nodes and the number of edges.
Each of the next  lines contains two space-separated integers,  and , describing an edge connecting node  to node .
The last line contains a single integer, , the index of the starting node.
Constraints

Output Format

For each of the  queries, print a single line of  space-separated integers denoting the shortest distances to each of the  other nodes from starting position . These distances should be listed sequentially by node number (i.e., ), but should not include node . If some node is unreachable from , print  as the distance to that node.

Sample Input

2
4 2
1 2
1 3
1
3 1
2 3
2
Sample Output

6 6 -1
-1 6
Explanation

We perform the following two queries:

The given graph can be represented as:
image
where our start node, , is node . The shortest distances from  to the other nodes are one edge to node , one edge to node , and there is no connection to node .
The given graph can be represented as:
image
where our start node, , is node . There is only one edge here, so node  is unreachable from node  and node  has one edge connecting it to node . We then print node 's distance to nodes  and  (respectively) as a single line of space-separated integers: -1 6.

Note: Recall that the actual length of each edge is , and we print  as the distance to any node that's unreachable from .
"""

from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(list)

    def connect(self,x,y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.n)]
        unvisited = set([i for i in range(self.n)])
        queue = []
        distances[root] = 0
        unvisited.remove(root)
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)
            children = self.edges[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    queue.append(child)

        distances.pop(root)
        print(" ".join(map(str,distances)))

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)




stop = True