"""
coding: utf-8
Created on 29/10/2020

@author: github.com/eduardormonteiro

From: MIT 6.00.1x Introduction to Computer Science and Programming Using Python
"""
import time


def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        # print(L)
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
    return L

def selection_sort(L):
    suffixStart = 0
    while suffixStart != len(L):
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
    return L

import operator

def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
    

test = [1, 5, 3, 8, 4, 2, 9, 6]
test = [1, 5, 3, 8, 4, 2, 9, 6, 15, 19, 7, 17, 14, 18, 16, 13]

t0 = time.perf_counter() #also measures wall-clock time but can be reset
testSorted = sorted(test)
t1 = time.perf_counter() - t0
print("list:" + str(testSorted) + " - time:{0:.6f}".format(t1))

t0 = time.perf_counter() #also measures wall-clock time but can be reset
testSorted = bubble_sort(test)
t1 = time.perf_counter() - t0
print("list:" + str(testSorted) + " - time:{0:.6f}".format(t1))

t0 = time.perf_counter() #also measures wall-clock time but can be reset
testSorted = selSort(test)
t1 = time.perf_counter() - t0
print("list:" + str(testSorted) + " - time:{0:.6f}".format(t1))

t0 = time.perf_counter() #also measures wall-clock time but can be reset
testSorted = selection_sort(test)
t1 = time.perf_counter() - t0
print("list:" + str(testSorted) + " - time:{0:.6f}".format(t1))

t0 = time.perf_counter() #also measures wall-clock time but can be reset
testSorted = mergeSort(test)
t1 = time.perf_counter() - t0
print("list:" + str(testSorted) + " - time:{0:.6f}".format(t1))

t0 = time.perf_counter() #also measures wall-clock time but can be reset
testSorted = test[:]
testSorted.sort()
t1 = time.perf_counter() - t0
print("list:" + str(testSorted) + " - time:{0:.6f}".format(t1))

stop = True
