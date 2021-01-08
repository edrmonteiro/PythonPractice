"""
Day 10: Binary Numbers
https://www.hackerrank.com/challenges/30-binary-numbers/problem?h_r=email&unlock_token=d87964fc64f98f2a47aa248807129494e8b8804c&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.

Example

The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
Explanation

Sample Case 1:
The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2:
The binary representation of  is , so the maximum number of consecutive 's is .

"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = str(bin(int(n)))[2:]
    count = 0
    maxcount = 0
    for b in binary:
        if b == '1':
            count += 1
        else:
            count = 0
        maxcount = max(maxcount, count)
    print (maxcount)