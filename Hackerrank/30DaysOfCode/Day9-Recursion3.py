"""
Hackerrank
Day 9: Recursion 3
https://www.hackerrank.com/challenges/30-recursion/problem?h_r=email&unlock_token=bc6d5f3963afb26ed0b2f69c3f4f3ddb1826e1b2&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder

Objective
Today, we are learning about an algorithmic concept called recursion. Check out the Tutorial tab for learning materials and an instructional video.

Recursive Method for Calculating Factorial
Function Description
Complete the factorial function in the editor below. Be sure to use recursion.

factorial has the following paramter:

int n: an integer
Returns

int: the factorial of 
Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

Input Format

A single integer,  (the argument to pass to factorial).

Constraints

Your submission must contain a recursive function named factorial.
Sample Input

3
Sample Output

6
Explanation

Consider the following steps. After the recursive calls from step 1 to 3, results are accumulated from step 3 to 1.



"""

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()