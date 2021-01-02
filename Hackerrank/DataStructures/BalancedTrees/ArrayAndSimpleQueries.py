"""
Hackerrank
Array and simple queries
https://www.hackerrank.com/challenges/array-and-simple-queries/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen

Given two numbers  and .  indicates the number of elements in the array  and  indicates number of queries. You need to perform two types of queries on the array .

You are given  queries. Queries can be of two types, type 1 and type 2.

Type 1 queries are represented as 1 i j : Modify the given array by removing elements from  to  and adding them to the front.

Type 2 queries are represented as 2 i j : Modify the given array by removing elements from  to  and adding them to the back.

Your task is to simply print  of the resulting array after the execution of  queries followed by the resulting array.

Note While adding at back or front the order of elements is preserved.

Input Format

First line consists of two space-separated integers,  and .
Second line contains  integers, which represent the elements of the array.
 queries follow. Each line contains a query of either type 1 or type 2 in the form 

Constraints


Output Format

Print the absolute value i.e.  in the first line.
Print elements of the resulting array in the second line. Each element should be seperated by a single space.

Sample Input

8 4
1 2 3 4 5 6 7 8
1 2 4
2 3 5
1 4 7
2 1 4
Sample Output

1
2 3 6 5 7 8 4 1
Explanation

Given array is .
After execution of query , the array becomes .
After execution of query , the array becomes .
After execution of query , the array becomes .
After execution of query , the array becomes .
Now  is  i.e.  and the array is 
"""


# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
        
#     def createTree(self, array):
#         node = self
#         for item in array:
#             node.next = Node(item)
#             nodeTemp = node
#             node = node.next
#             node.prev = nodeTemp
#         return node

#     def moveSliceBegin(self, i, j):
#         slice1Begin = slice1End = self
#         node = self
#         index = 0
#         while i - 1 > index:
#             slice1End = node
#             node = node.next
#             index += 1
#         slice2Begin = slice2End = node        
#         while j > index:
#             slice2End = node
#             node = node.next
#             index += 1
#         slice3Start = node
#         while node.next != None:            
#             node = node.next
#         slice3End = node
#         slice3End.next = None
#         if slice1Begin != slice2Begin:
#             slice2End.next = slice1Begin
#             slice1End.next = slice3Start
#         return slice2Begin

#     def moveSliceEnd(self, i, j):
#         slice1Begin = slice1End = self
#         node = self
#         index = 0
#         while i - 1 > index:
#             slice1End = node
#             node = node.next
#             index += 1
#         slice2Begin = slice2End = node        
#         while j > index:
#             slice2End = node
#             node = node.next
#             index += 1
#         slice3Start = node
#         while node.next != None:            
#             node = node.next
#         slice3End = node        
#         slice3End.next = slice2Begin
#         slice2End.next = None
#         if slice1Begin == slice2Begin:
#             return slice3Start
#         slice1End.next = slice3Start
#         return slice1Begin

#     def printTree(self):
#         node = self
#         first = node.data
#         items = []
#         while node.next != None:
#             items.append(node.data)
#             node = node.next
#         items.append(node.data)
#         print(abs(first - node.data))
#         print(' '.join(map(str, items)))

# A = [1, 2, 3, 4, 5, 6, 7, 8]
# queries = [[1, 2, 4],[2, 3, 5], [1, 4, 7], [2, 1, 4]]

# A =  [20000, 14207, 12040, 26476, 29558, 14636, 20025, 12657, 25055, 16071, 10278, 19381, 25145, 31369, 16306, 8410, 6828, 1990, 22897, 24439]
# queries = [[2, 5, 11],[1, 8, 13],[2, 9, 13],[1, 6, 11],[2, 2, 10],[1, 1, 3],[2, 1, 3],[1, 3, 7],[2, 6, 14],[1, 7, 10],[2, 4, 6],[1, 7, 14],[2, 2, 11],[1, 6, 10],[2, 4, 6],[1, 9, 12],[2, 4, 11],[1, 2, 8],[2, 7, 10],[1, 8, 9]]
# for query in queries:
#     if query[0] == 1:
#         temp = A[query[1]-1:query[2]]
#         del A[query[1]-1:query[2]]
#         temp.extend(A)
#         A = temp
#     elif query[0] == 2:
#         temp = A[query[1]-1:query[2]]
#         del A[query[1]-1:query[2]]
#         A.extend(temp)

# print(abs(A[0] - A[-1]))
# print(*A)

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def createTree(self, array):
        node = self
        for item in array:
            node.next = Node(item)
            nodeTemp = node
            node = node.next
            node.prev = nodeTemp
        return node

    def moveSliceBegin(self, i, j):
        if i == 1:
            return self
        slice1Begin = self
        node = self
        index = 0
        while i - 1 > index:
            node = node.next
            index += 1
        slice1End = node.prev
        slice2Begin = node        
        while j > index:            
            node = node.next
            index += 1
        slice2End = node.prev
        slice3Begin = node
        # while node.next != None:            
        #     node = node.next
        # slice3End = node
        # slice3End.next = None
        #slice3End.prev = slice2End
        slice2Begin.prev = None        
        slice2End.next = slice1Begin
        slice1Begin.prev = slice2End
        #slice2End.prev = slice1End
        slice1End.next = slice3Begin
        slice3Begin.prev = slice1End
        return slice2Begin

    def moveSliceEnd(self, i, j):
        slice1Begin = slice1End = self
        node = self
        index = 0
        while i - 1 > index:
            slice1End = node
            node = node.next
            index += 1
        slice2Begin = slice2End = node        
        while j > index:
            slice2End = node
            node = node.next
            index += 1
        slice3Start = node
        while node.next != None:            
            node = node.next
        slice3End = node        
        slice3End.next = slice2Begin
        slice2End.next = None
        if slice1Begin == slice2Begin:
            return slice3Start
        slice1End.next = slice3Start
        return slice1Begin

    def printTree(self):
        node = self
        first = node.data
        items = []
        while node.next != None:
            items.append(node.data)
            node = node.next
        items.append(node.data)
        print(abs(first - node.data))
        print(' '.join(map(str, items)))


A = [1, 2, 3, 4, 5, 6, 7, 8]
queries = [[1, 2, 4],[2, 3, 5], [1, 4, 7], [2, 1, 4]]

# A =  [20000, 14207, 12040, 26476, 29558, 14636, 20025, 12657, 25055, 16071, 10278, 19381, 25145, 31369, 16306, 8410, 6828, 1990, 22897, 24439]
# queries = [[2, 5, 11],[1, 8, 13],[2, 9, 13],[1, 6, 11],[2, 2, 10],[1, 1, 3],[2, 1, 3],[1, 3, 7],[2, 6, 14],[1, 7, 10],[2, 4, 6],[1, 7, 14],[2, 2, 11],[1, 6, 10],[2, 4, 6],[1, 9, 12],[2, 4, 11],[1, 2, 8],[2, 7, 10],[1, 8, 9]]

n, m = map(int, input().split())
A = list(map(int, input().split()))
queries = []
for _ in range(m):
    queries.append([int(i) for i in input().split()])

root = Node(A[0])
root.createTree(A[1:])
root.printTree()
for type, i, j in queries:
    if type == 1:
        root = root.moveSliceBegin(i, j)
        root.printTree()
    elif type == 2:
        root = root.moveSliceEnd(i, j)
        root.printTree()
root.printTree()

stop = True

