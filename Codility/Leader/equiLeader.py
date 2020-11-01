"""
coding: utf-8
Created on 31/10/2020

@author: github.com/eduardormonteiro

From: Codility Lessons
"""


# A non-empty array A consisting of N integers is given.

# The leader of this array is the value that occurs in more than half of the elements of A.

# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:

# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

# For example, given:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].



def solution(A):
    dominator = 0
    sequence = 0
    for i, item in enumerate(A):
        if sequence == 0:
            dominator = item
            sequence += 1
        elif item == dominator:
            sequence += 1
        else:
            sequence -= 1
    occurrences = A.count(dominator)

    left = 0
    equiLeaders = 0
    for i, item in enumerate(A):
            
        if item == dominator:
            left += 1
            
        if left > (i + 1) // 2 and (occurrences - left) > (len(A) - (i + 1)) // 2:
            equiLeaders += 1

    return equiLeaders


A = [4, 3, 4, 4, 4,  2]
print(solution(A))

A = [3, 2, 3, 4, 3, 3, 3, -1]
print(solution(A))

print(solution([3,0,1,1,4,1,1]))

stop = True