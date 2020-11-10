
"""
coding: utf-8
Created on 30/10/2020

@author: github.com/edrmonteiro

From: Codility Lessons
"""

# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

# For example, array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# contains the following example slices:

# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].


#  (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1)


def solution(A):
    index = 0
    minAverage = (A[0] + A[1])/2
    for i, item in enumerate(A):
        try:
            average2 = (item + A[i + 1]) / 2
            if minAverage > average2:
                minAverage = average2
                index = i
            
            average3 = (item + A[i + 1] + A[i + 2]) / 3
            if minAverage > average3:
                minAverage = average3
                index = i                

        except:
            break
    return index



A = [4, 2, 2, 5, 1, 5, 8]
print(solution(A)) #1

A = [4, 5, 2, 4, 1, 5, 8, 2, 4, 1]
print(solution(A))  #2

A = [-3, -5, -8, -4, -10] 
print(solution(A))  #2

stop = True

