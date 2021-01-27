"""
Hackerrank
Day 29: Bitwise AND
https://www.hackerrank.com/challenges/30-bitwise-and/problem?h_r=email&unlock_token=31d4359f28e8a32f2f9b4bc0232b968bbaf43253&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
Objective
Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given set . Find two integers,  and  (where ), from set  such that the value of  is the maximum possible and also less than a given integer, . In this case,  represents the bitwise AND operator.

Input Format

The first line contains an integer, , the number of test cases.
Each of the  subsequent lines defines a test case as  space-separated integers,  and , respectively.

Constraints

Output Format

For each test case, print the maximum possible value of  on a new line.

Sample Input

3
5 2
8 5
2 2
Sample Output

1
4
0
Explanation

All possible values of  and  are:
The maximum possible value of  that is also  is , so we print  on a new line.

"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #t = int(input())
    t = 1
    for t_itr in range(t):
        # nk = input().split()

        # n = int(nk[0])

        # k = int(nk[1])

        n = 5
        k = 2
        
        #A = [i for i in range(1, n + 1)]
        # value = 0
        # for a in A:
        #     B = A[:]            
        #     B.pop(B.index(a))
        #     for b in B:
        #         if a&a < k:
        #             value = max(value, a&b)
        # print(value)
        print(k-1 if ((k-1) | k) <= n else k-2)