"""
Day 3: Intro to Conditional Statements
https://www.hackerrank.com/challenges/30-conditional-statements/problem?h_r=email&unlock_token=fb8ad1c2d78191b5fb6bdfbc00fee9e249523cfe&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder

Objective
In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird
Explanation

Sample Case 0: 
 is odd and odd numbers are weird, so we print Weird.

Sample Case 1: 
 and  is even, so it is not weird. Thus, we print Not Weird.
"""


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    even = True if N % 2 == 0 else False
    if not even:
        print ("Weird")
    elif 2 <= N <= 5:
        print ("Not Weird")
    elif 6 <= N <= 20:
        print ("Weird")
    elif 20 < N:
        print ("Not Weird")