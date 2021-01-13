"""
Max Transform
https://www.hackerrank.com/challenges/max-transform/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen

Transforming data into some other data is typical of a programming job. This problem is about a particular kind of transformation which we'll call the max transform.

Let  be a zero-indexed array of integers. For , let  denote the subarray of  from index  to index , inclusive.

Let's define the max transform of  as the array obtained by the following procedure:

Let  be a list, initially empty.
For  from  to :
For  from  to :
Let .
Append  to the end of .
Return .
The returned array is defined as the max transform of . We denote it by .

Complete the function solve that takes an integer array  as input.

Given an array , find the sum of the elements of , i.e., the max transform of the max transform of . Since the answer may be very large, only find it modulo .

Input Format

The first line of input contains a single integer  denoting the length of .

The second line contains  space-separated integers  denoting the elements of .

Constraints

Subtasks

For  of the total score, 
Output Format

Print a single line containing a single integer denoting the answer.

Sample Input 0

3
3 2 1
Sample Output 0

58
Explanation 0

In the sample case, we have:

Therefore, the sum of the elements of  is .
"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(A):
    # Return the sum of S(S(A)) modulo 10^9+7.


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    result = solve(A)

    fptr.write(str(result) + '\n')

    fptr.close()


