"""
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].
"""

# from collections import defaultdict
# def solution(A):
#     # write your code in Python 3.6
#     times = [0] * len(A)
#     popIdx = len(A) - 1
#     while A:
#         number = A.pop()
#         count = 0
#         for i, item in enumerate(A):
#             if number % item != 0:
#                 times[popIdx] += 1
#             if item % number != 0:
#                 times[i] += 1
#         popIdx -= 1
#     return times


"""
55%
[3, 1, 2, 3, 6]
             6  [1,1,1,1,0] 
          3     [1,2,2,2,0] 
       2        [2,3,3,2,0] 
    1           [2,4,3,2,0] 
3               [2,4,3,2,0] 

                [2,4,3,2,0]

"""
def get_divisors(n):
    froot = int(n**.5)
    divs = set()
    # reverse through possible divisors which are lower than root(n)
    while froot > 0:
        if not n%froot:
            divs.add(froot)
            divs.add(n//froot) # Catch the higher divisor on the other side of froot
        froot-=1
    return divs

def solution(A):
    N = len(A)
    int_count = {}
    
    # O(N) scan to count number frequency
    for i in range(N):
        int_count[A[i]] = int_count.get(A[i], 0) + 1
    
    # Create an array for every i non-divisor count
    div_count = {}
    
    for i, freq in int_count.items():
        divs = get_divisors(i)
        num_divs = 0
        for d in divs:
            num_divs += int_count.get(d, 0)
        div_count[i] = N-num_divs # N -  divisors = non-divisors :-)
        
    return [div_count[A[i]] for i in range(N)]


print(solution([12, 1, 2, 3, 6]))
print(solution([3, 1, 2, 3, 6]))

stop = True

