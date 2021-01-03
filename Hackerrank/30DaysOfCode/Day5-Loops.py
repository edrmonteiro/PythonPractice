"""
Day 5: Loops
https://www.hackerrank.com/challenges/30-loops/problem?h_r=email&unlock_token=d60259ce92e322fd978cfb2f35b1040404e6a8d2&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder

Objective
In this challenge, we will use loops to do some math. Check out the Tutorial tab to learn more.

Task
Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.

Example

The printout should look like this:

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
Input Format

A single integer, .

Constraints

Output Format

Print  lines of output; each line  (where ) contains the  of  in the form:
n x i = result.

Sample Input

2
Sample Output

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

"""


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for i in range(10):
        print("%d x %d = %d" % (n, i + 1, (n * (i+1))))
        
