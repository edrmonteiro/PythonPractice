"""
Hackerrank
Day 26: Nested Logic
https://www.hackerrank.com/challenges/30-nested-logic/problem?h_r=email&unlock_token=0d4c8c4dd306892b7113114a840c37252e55eace&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
Objective
Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing.

Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
Example
 returned date
 due date

The book is returned on time, so no fine is applied.

 returned date
 due date

The book is returned in the following year, so the fine is a fixed 10000.

Input Format

The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned.
The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).

Constraints

Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)
Sample Output

45
Explanation

Given the following return dates:
Returned: 
Due: 

Because , it is less than a year late.
Because , it is less than a month late.
Because , it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be . We then print the result of  as our output.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
# d1, m1, y1 = map(int, input().split())
# d2, m2, y2 = map(int, input().split())
d2, m2, y2 = map(int, "31 12 2009".split())
d1, m1, y1 = map(int, "1 1 2010".split())

# d2, m2, y2 = map(int, "2 6 2014".split())
# d1, m1, y1 = map(int, "5 7 2014".split())

if y2 - y1 > 0:
    print ("10000")
else:
    if int(str(y2) + str("{:02d}".format(m2))) - int(str(y1) + str("{:02d}".format(m1))) > 0:
        print((m2-m1)*500)
    else:
        if int(str(y2) + str("{:02d}".format(m2)) + str("{:02d}".format(d2))) - int(str(y1) + str("{:02d}".format(m1))+ str("{:02d}".format(d1))) > 0:
            print((d2-d1)*15)
        else:
            print (0)

stop = True