"""
coding: utf-8
Created on 02/11/2020

@author: github.com/edrmonteiro

From: Codility Lessons
"""
# Nesting
# A string S consisting of N characters is called properly nested if:

# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

# For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..1,000,000];
# string S consists only of the characters "(" and/or ")".

def solution(S):
    openned = 0
    if len(S) % 2 != 0:
        return 0
    for char in S:
        if char == "(":
            openned += 1
        elif char == ")":
            openned -= 1
            if openned < 0:
                return 0
    if openned != 0:
        return 0
    return 1

S = "(()(())())"
print(solution(S))


S = "())"
print(solution(S))


stop = True