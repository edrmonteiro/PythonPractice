"""
From: BetterProgramming Educative Team
https://medium.com/better-programming/cracking-the-amazon-interview-cf6a6c5f954a

1. Find the missing number in the array
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. 
You have to find x. The input array is not sorted. Look at the below array and view the solution in Python. 
Click here to view the solution in C++, Java, JavaScript, and Ruby.

ex:
3 7 1 2 8 4 5
n = 8 missing number = 6

"""

# from ramdom import random
import random

def find_missing(input):
    # calculate sum of all elements
    # in input list
    sum_of_elements = sum(input)
    # There is exactly 1 number missing
    n = len(input) + 1
    actual_sum = (n * ( n + 1 ) ) / 2
    return actual_sum - sum_of_elements

def test(n):
    missing_element = random.randint(1, n)
    v = []
    for i in range(1, n):
        if i != missing_element:
            v.append(i)
    actual_missing = find_missing(v)
    print("Expected Missing = ", missing_element, " Actual Missing = ", actual_missing)
    assert missing_element == actual_missing


def main():
    for n in range(1, 10):
        test(20)
main()





