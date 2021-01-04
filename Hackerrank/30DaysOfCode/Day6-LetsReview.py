"""
Day 6: Let's Review
https://www.hackerrank.com/challenges/30-review-loop/problem?h_r=email&unlock_token=e06f99a674f05b5691a9a70adfc55d5599b5ccb4&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
Objective
Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.

Example

Print abc def

Input Format

The first line contains an integer,  (the number of test cases).
Each line  of the  subsequent lines contain a string, .

Constraints

Output Format

For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.

Sample Input

2
Hacker
Rank
Sample Output

Hce akr
Rn ak
Explanation

Test Case 0: 

The even indices are , , and , and the odd indices are , , and . 
We then print a single line of  space-separated strings; the first string contains the ordered characters from 's even indices (), 
and the second string contains the ordered characters from 's odd indices ().

Test Case 1: 

The even indices are  and , and the odd indices are  and . 
We then print a single line of  space-separated strings; the first string contains the ordered characters from 's even indices (), 
and the second string contains the ordered characters from 's odd indices ().

"""

n = int(input())

for j in range(n):
    s = input()
    even = ''
    odd = ''
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print (even, odd)

