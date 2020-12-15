"""
The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, you must perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the list's updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
Input Format

The first line contains a single integer, , denoting the number of integers in the data stream.
Each line  of the  subsequent lines contains an integer, , to be added to your list.

Constraints

Output Format

After each new integer is added to the list, print the list's updated median on a new line as a single double-precision number scaled to  decimal place (i.e.,  format).

Sample Input

6
12
4
5
3
8
7
Sample Output

12.0
8.0
5.0
4.5
5.0
6.0
Explanation

There are  integers, so we must print the new median on a new line as each integer is added to the list:



"""

# import os
# import sys

# #
# # Complete the runningMedian function below.
# #
# def runningMedian(a):
#     #
#     # Write your code here.
#     #

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a_count = int(input())

#     a = []

#     for _ in range(a_count):
#         a_item = int(input())
#         a.append(a_item)

#     result = runningMedian(a)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()



# def runningMedian(a):

# // - We use 2 Heaps to keep track of median
# // - We make sure that 1 of the following conditions is always true:
# //    1) maxHeap.size() == minHeap.size()
# //    2) maxHeap.size() - 1 = minHeap.size()

# public class Solution {

    # public static void main(String[] args) {
    #     Scanner scan = new Scanner(System.in);
    #     int n = scan.nextInt();
    #     int [] array = new int[n];
    #     for (int i = 0; i < n; i++) {
    #         array[i] = scan.nextInt();
    #     }
    #     scan.close();
    #     medianTracker(array);
    # }
    
# def runningMedian(array):
#     def addNumber(n):
#         if len(minHeap) == 0 or n < minHeap[-1]:
#             minHeap.append(n)
#         else:
#             maxHeap.append(n)

#     def rebalance ():
#         biggerHeap = minHeap if len(minHeap) > len(maxHeap) else maxHeap
#         smallerHeap = maxHeap if len(minHeap) > len(maxHeap) else minHeap
#         if len(biggerHeap) - len(smallerHeap) >= 2:
#             smallerHeap.append(biggerHeap.pop)

#     def getMedian():
#         biggerHeap = minHeap if len(minHeap) > len(maxHeap) else maxHeap
#         smallerHeap = maxHeap if len(minHeap) > len(maxHeap) else minHeap

#         if len(biggerHeap) == len(smallerHeap):
#             return (biggerHeap[-1] + smallerHeap[-1]) / 2.0
#         else:   # maxHeap must have more elements than minHeap
#             return biggerHeap[-1]
#     maxHeap = []    # keeps track of the SMALL numbers
#     minHeap = []    # keeps track of the LARGE numbers
#     medians = [0] * len(array)
#     for i in range(0, len(array)):
#         addNumber(array[i])
#         rebalance ()
#         medians[i] = getMedian()
#     print(medians)



# def runningMedian(array):
#     def addNumber(n):
#         if len(maxHeap) == 0:
#             maxHeap.append(n)
#         elif len(maxHeap) == len(minHeap):
#             if n < minHeap[0]:
#                 maxHeap.append(n)
#             else:
#                 minHeap.append(n)
#                 maxHeap.append(minHeap.pop(0))
#         elif len(maxHeap) > len(minHeap):
#             if n > maxHeap[0]:
#                 minHeap.append(n)
#             else:
#                 maxHeap.append(n)
#                 minHeap.append(maxHeap.pop(0))
#         # maxHeap will never have fewer elements than minHeap

#     def getMedian():
#         if len(maxHeap) == 0:
#             return 0
#         elif len(maxHeap) == len(minHeap):
#             return (maxHeap[0] + minHeap[0]) / 2.0
#         else:   # maxHeap must have more elements than minHeap
#             return maxHeap[0]
#     maxHeap = []    # keeps track of the SMALL numbers
#     minHeap = []    # keeps track of the LARGE numbers
#     for i in range(0, len(array)):
#         addNumber(array[i])
#         print (getMedian())



# class Heap(object):
# 	def __init__(self):
# 		self.lower = []
# 		self.upper = []

# 	def find_parent(self, lastIndex):
# 		if lastIndex == 0:
# 			return -1
# 		if lastIndex % 2 == 0:
# 			return (lastIndex - 2) // 2
# 		return (lastIndex - 1) // 2

# 	def find_min_child(self, index):
# 		l = (index * 2) + 1
# 		r = (index * 2) + 2
# 		if l >= len(self.upper) and r >= len(self.upper):
# 			return -1
# 		if l >= len(self.upper):
# 			return r
# 		if r >= len(self.upper):
# 			return l
# 		return l if self.upper[l] < self.upper[r] else r

# 	def find_max_child(self, index):
# 		l = (index * 2) + 1
# 		r = (index * 2) + 2
# 		if l >= len(self.lower) and r >= len(self.lower):
# 			return -1
# 		if l >= len(self.lower):
# 			return r
# 		if r >= len(self.lower):
# 			return l
# 		return l if self.lower[l] > self.lower[r] else r

# 	def max_pop(self):
# 		pop_value = self.lower[0]
# 		self.lower[0] = self.lower.pop()
# 		n_i = 0
# 		while True:
# 			r_i = self.find_max_child(n_i)
# 			if r_i == -1:
# 				break
# 			if self.lower[n_i] < self.lower[r_i]:
# 				self.lower[n_i], self.lower[r_i] = self.lower[r_i], self.lower[n_i]
# 				n_i = r_i
# 			else:
# 				break
# 		return pop_value

# 	def min_pop(self):
# 		pop_value = self.upper[0]
# 		self.upper[0] = self.upper.pop()
# 		n_i = 0
# 		while True:
# 			r_i = self.find_min_child(n_i)
# 			if r_i == -1:
# 				break
# 			if self.upper[n_i] > self.upper[r_i]:
# 				self.upper[n_i], self.upper[r_i] = self.upper[r_i], self.upper[n_i]
# 				n_i = r_i
# 			else:
# 				break
# 		return pop_value

# 	def balance(self):
# 		if abs(len(self.lower) - len(self.upper)) >= 2:
# 			if len(self.upper) < len(self.lower):
# 				self.min_insert(self.max_pop())
# 			else:
# 				self.max_insert(self.min_pop())
                
# 	def max_up(self, c, t):
# 		self.lower[c], self.lower[t] = self.lower[t], self.lower[c]
# 		c = t
# 		while True:
# 			parent_index = self.find_parent(c)
# 			if parent_index == -1:
# 				break
# 			if self.lower[parent_index] > self.lower[c]:
# 				break
# 			t = parent_index
# 			self.lower[c], self.lower[t] = self.lower[t], self.lower[c]
# 			c = t

# 	def min_up(self, c, t):
# 		self.upper[c], self.upper[t] = self.upper[t], self.upper[c]
# 		c = t
# 		while True:
# 			parent_index = self.find_parent(c)         
# 			if parent_index == -1:
# 				break
# 			if self.upper[parent_index] < self.upper[c]:
# 				break
# 			t = parent_index
# 			self.upper[c], self.upper[t] = self.upper[t], self.upper[c]
# 			c = t                

# 	def max_insert(self, value):
# 		self.lower.append(value)
# 		parent_index = self.find_parent(len(self.lower) - 1)
# 		if parent_index != -1:
# 			if self.lower[parent_index] < value:
# 				self.max_up(len(self.lower) - 1, parent_index)                

# 	def min_insert(self, value):
# 		self.upper.append(value)
# 		parent_index = self.find_parent(len(self.upper) - 1)
# 		if parent_index != -1:
# 			if self.upper[parent_index] > value:
# 				self.min_up(len(self.upper) - 1, parent_index)

# 	def median(self):
# 		if len(self.lower) == len(self.upper):
# 			return (float(self.lower[0]) + float(self.upper[0])) / 2.0
# 		elif len(self.lower) > len(self.upper):
# 			return float(self.lower[0])
# 		else:
# 			return float(self.upper[0])

# 	def insert(self, value):
# 		if len(self.lower) == 0 or value < self.lower[0]:
# 			self.max_insert(value)
# 		else:
# 			self.min_insert(value)
# 		self.balance()
# 		return self.median()

# def runningMedian(a):
#     heap = Heap()
#     median = [0] * len(a)
#     for i, number in enumerate(a):
#         median[i] = heap.insert(number)
#     return median

# #a = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         # [10.0, 5.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
# a = [12, 4, 5, 3, 8, 7]
# print(runningMedian(a))     
# stop = True

from heapq import heappush as push, heappushpop as pushpop

class Heap:
	def __init__(self):
		self.upper = []
		self.lower = []
        
	def median(self):
		if len(self.upper) > len(self.lower):
			return float('%.1f' % self.upper[0])
		else:
			return float('%.1f' % round((self.upper[0] - self.lower[0]) / 2, 1))

	def add(self, value):
		value = pushpop(self.upper, value)
		value = -pushpop(self.lower, -value)
		if len(self.upper) <= len(self.lower):
			push(self.upper, value)
		else:
			push(self.lower, -value)

def runningMedian(a):
	heap = Heap()
	median = [0] * len(a)
	for i, number in enumerate(a):
		heap.add(number)
		median[i] = heap.median()
	return median

#a = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         # [10.0, 5.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
a = [12, 4, 5, 3, 8, 7]		# [12.0, 8.0, 5.0, 4.5, 5.0, 6.0]
print(runningMedian(a))     
stop = True


# import sys

class Heap1(object):
	def __init__(self):
		self.lower = []
		self.upper = []

	def parentIndex(self, lastIndex):
		if lastIndex == 0:
			return -1
		if lastIndex % 2 == 0:
			return (lastIndex - 2) // 2
		return (lastIndex - 1) // 2

	def find_min_child(self, index):
		l = (index * 2) + 1
		r = (index * 2) + 2
		if l >= len(self.upper) and r >= len(self.upper):
			return -1
		if l >= len(self.upper):
			return r
		if r >= len(self.upper):
			return l
		return l if self.upper[l] < self.upper[r] else r

	def find_max_child(self, index):
		l = (index * 2) + 1
		r = (index * 2) + 2
		if l >= len(self.lower) and r >= len(self.lower):
			return -1
		if l >= len(self.lower):
			return r
		if r >= len(self.lower):
			return l
		return l if self.lower[l] > self.lower[r] else r

	def max_pop(self):
		pop_value = self.lower[0]
		self.lower[0] = self.lower.pop()
		n_i = 0
		while True:
			r_i = self.find_max_child(n_i)
			if r_i == -1:
				break
			if self.lower[n_i] < self.lower[r_i]:
				self.lower[n_i], self.lower[r_i] = self.lower[r_i], self.lower[n_i]
				n_i = r_i
			else:
				break
		return pop_value

	def min_pop(self):
		pop_value = self.upper[0]
		self.upper[0] = self.upper.pop()
		n_i = 0
		while True:
			r_i = self.find_min_child(n_i)
			if r_i == -1:
				break
			if self.upper[n_i] > self.upper[r_i]:
				self.upper[n_i], self.upper[r_i] = self.upper[r_i], self.upper[n_i]
				n_i = r_i
			else:
				break
		return pop_value

	def balance(self):
		if abs(len(self.lower) - len(self.upper)) >= 2:
			if len(self.upper) < len(self.lower):
				self.upperInsert(self.max_pop())
			else:
				self.lowerInsert(self.min_pop())
                
	def lowerReorder(self, c, t):
		self.lower[c], self.lower[t] = self.lower[t], self.lower[c]
		c = t
		while True:
			parent_index = self.parentIndex(c)
			if parent_index == -1:
				break
			if self.lower[parent_index] > self.lower[c]:
				break
			self.lower[c], self.lower[parent_index] = self.lower[parent_index], self.lower[c]
			c = parent_index

	def upperReorder(self, c, t):
		self.upper[c], self.upper[t] = self.upper[t], self.upper[c]
		c = t
		while True:
			parent_index = self.parentIndex(c)         
			if parent_index == -1:
				break
			if self.upper[parent_index] < self.upper[c]:
				break
			t = parent_index
			self.upper[c], self.upper[t] = self.upper[t], self.upper[c]
			c = t                

	def lowerInsert(self, value):
		self.lower.append(value)
		parent_index = self.parentIndex(len(self.lower) - 1)
		if parent_index != -1:
			if self.lower[parent_index] < value:
				self.lowerReorder(len(self.lower) - 1, parent_index)                

	def upperInsert(self, value):
		self.upper.append(value)
		parent_index = self.parentIndex(len(self.upper) - 1)
		if parent_index != -1:
			if self.upper[parent_index] > value:
				self.upperReorder(len(self.upper) - 1, parent_index)

	def median(self):
		if len(self.lower) == len(self.upper):
			return (float(self.lower[0]) + float(self.upper[0])) / 2.0
		elif len(self.lower) > len(self.upper):
			return float(self.lower[0])
		else:
			return float(self.upper[0])

	def insert(self, value):
		if len(self.lower) == 0 or value < self.lower[0]:
			self.lowerInsert(value)
		else:
			self.upperInsert(value)
		self.balance()
		return self.median()

def runningMedian1(a):
    heap = Heap1()
    median = [0] * len(a)
    for i, number in enumerate(a):
        median[i] = heap.insert(number)
    return median

#a = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         # [10.0, 5.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
a = [12, 4, 5, 3, 8, 7]
print(runningMedian1(a))     
stop = True


import sys

def runningMedian2(a):
    def down(heap):
        c = len(heap) - 1
        p = (c - 1) >> 1
        while c > 0 and heap[c] < heap[p]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = (c - 1) >> 1

    def up(heap):
        p = 0
        while 2 * p + 1 < len(heap):
            c = 2 * p + 1
            if c + 1 < len(heap) and heap[c] > heap[c + 1]:
                c += 1        
            if heap[p] > heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
                p = c
            else:
                break
            
    def balance():
        if  len(maxHeap) < len(minHeap):
            maxHeap.extend([-minHeap[0]])
            down(maxHeap)
            minHeap[0] = minHeap[-1]
            minHeap.pop()
            up(minHeap)
        elif len(maxHeap) > len(minHeap) + 1:
            minHeap.extend([-maxHeap[0]])
            down(minHeap)
            maxHeap[0] = maxHeap[-1]
            maxHeap.pop()
            up(maxHeap)
    
    def add(n):
        if not maxHeap:
            maxHeap.append(n)
        elif n > maxHeap[0]:
            maxHeap.append(n)
            down(maxHeap)
        else:
            minHeap.append(-n)
            down(minHeap)
            
    def getMedian():
        if (len(maxHeap) + len(minHeap)) % 2 == 0:
            return float('%.1f' % round((maxHeap[0] - minHeap[0]) / 2, 1))
        else:
            return float('%.1f' % maxHeap[0])

    maxHeap = []
    minHeap = []    
    median = [0] * len(a)
    for i, item in enumerate(a):
        add(item)
        balance()
        median[i] = getMedian()
    return median

a = [12, 4, 5, 3, 8, 7]
print(runningMedian2(a))
stop = True



