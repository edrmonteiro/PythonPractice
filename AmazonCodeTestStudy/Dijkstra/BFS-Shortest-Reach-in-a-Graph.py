"""
https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
BFS: Shortest Reach in a Graph
Consider an undirected graph consisting of  nodes where each node is labeled from  to  and the edge between any two nodes is always of length . 
We define node  to be the starting position for a BFS. 
Given a graph, determine the distances from the start node to each of its descendants and return the list in node number order, ascending. 
If a node is disconnected, it's distance should be .

For example, there are  nodes in the graph with a starting node . The list of , and each has a weight of .


"""
import sys

class Graph:
    def __init__(self, n):
        self.vertices = n
        self.graph = [[-1 for column in range(n)] for row in range(n)]
        self.distances = [sys.maxsize] * n        
        self.visited = [False] * n

    def connect(self, x, y):
        self.graph[x][y] = 6
        self.graph[y][x] = 6
    
    def getNextNode(self):  
        smaller = sys.maxsize
        nextNode = -1       
        for i in range(self.vertices):            
            if (self.distances[i] - 1) < smaller and not self.visited[i]:
                smaller = self.distances[i]
                nextNode = i
        return nextNode
    
    def find_all_distances(self, currentNode):
        self.distances[currentNode] = 0
        for _ in range(self.vertices):
            self.visited[currentNode] = True
            for column in range(self.vertices):
                if self.graph[currentNode][column] > 0 and self.visited[column] == False and self.distances[column] > self.distances[currentNode] + self.graph[currentNode][column]: 
                        self.distances[column] = self.distances[currentNode] + self.graph[currentNode][column] 
            currentNode = self.getNextNode()
        answer = ''
        for item in self.distances:
            if item == sys.maxsize:
                item = -1
            if item != 0:
                answer += str(item) + ' '
        print (answer.strip())

vertices = 4
connections = [[1, 2], [1, 3]]
startNode = 1
graph = Graph(vertices)
for x, y in connections:
    graph.connect(x-1,y-1)
graph.find_all_distances(startNode-1)


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