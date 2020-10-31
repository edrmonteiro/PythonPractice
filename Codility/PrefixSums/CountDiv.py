"""
coding: utf-8
Created on 30/10/2020

@author: github.com/eduardormonteiro

From: Codility Lessons
"""

# DivCount

# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

from math import ceil, floor

def solution(A, B, K):
    start = ceil(A / K)
    end = floor(B / K)
    return end - start + 1 


A = 6
B = 11
K = 2
print(solution(A, B, K)) #3

A = 11
B = 345
K = 17
print(solution(A, B, K))   #20
A = 10
B = 10
K = 5
print(solution(A, B, K))   #1
A = 10
B = 10
K = 7
print(solution(A, B, K))   #0
A = 10
B = 10
K = 20
print(solution(A, B, K))   #0

A = 0
B = 0
K = 11
print(solution(A, B, K))   #1


stop = True


# 50% performance problems
# def solution(A, B, K):
#     count = 0
#     for i in range(A, B + 1):
#         if i % K == 0:
#             count += 1
#     return count