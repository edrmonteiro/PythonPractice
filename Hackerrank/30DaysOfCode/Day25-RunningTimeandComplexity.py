"""
Hackerrank
Day 25: Running Time and Complexity
https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?h_r=email&unlock_token=09d355406de58a7f7d683b0a2f88f08676c24829&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
Objective
Today we will learn about running time, also known as time complexity. Check out the Tutorial tab for learning materials and an instructional video.

Task
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it is  or .

Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code.

Input Format

The first line contains an integer, , the number of test cases.
Each of the  subsequent lines contains an integer, , to be tested for primality.

Constraints

Output Format

For each test case, print whether  is  or  on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: .
 is divisible by numbers other than  and itself (i.e.: , , , ), so we print  on a new line.

Test Case 1: .
 is only divisible  and itself, so we print  on a new line.

Test Case 2: .
 is only divisible  and itself, so we print  on a new line.
"""

def isPrime(number):
    if number == 1:
        return "Not prime"
    elif number == 2:
        return "Prime"
    elif number % 2 == 0:
        return "Not prime"
    i = 3
    while i**2 <= number :
        if number % i == 0:
            return "Not prime"
        i += 2
    return "Prime"


# T = int(input())
# for _ in range(T):
#     n = int(input())
#     print(isPrime(n))

N = [1000000007, 100000003, 1000003]
N = [79, 10]

#T = int(input())
for n in N:
    print(isPrime(n))

stop = True