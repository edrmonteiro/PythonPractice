"""
coding: utf-8
Created on 02/12/2020

@author: github.com/edrmonteiro

From: Codility Lessons
Challenge: ChocolatesByNumbers

Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..1,000,000,000].


"""

def getGreatestCommonDivisor(a, b):
    if b == 0:
        return a
    else:
        return getGreatestCommonDivisor(b, a % b)


def solution(N, M):
    return N // getGreatestCommonDivisor(N, M)




N = 10
M = 4
print(solution(N, M))

N = 1
M = 1
print(solution(N, M))


stop = True

# 50%
# def solution(N, M):
#     circle = [False] * N
#     count = 0
#     chocolate = 0
#     for i in range(0, N):
#         if circle[chocolate]:
#             return count
#         circle[chocolate] = True
#         count += 1        
#         chocolate = (chocolate + M) % N
#     return count