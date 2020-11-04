"""
coding: utf-8
Created on 02/11/2020

@author: github.com/eduardormonteiro

From: Codility Lessons
"""

# Brackets

# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

def solution(S):
    open = "({["
    close = ")}]"
    stack = []
    if len(S) % 2 != 0:
        return 0
    for char in S:
        if char in open:
            stack.append(char)
        elif char in close:
            if len(stack) == 0:
                return 0
            nextToClose = stack.pop()
            i = open.index(nextToClose)
            if close[i] != char:
                return 0
        else: 
            return 0
    if len(stack) != 0:
        return 0
    return 1


S = "{[()()]}"
print(solution(S))

S = "([)()]"
print(solution(S))


stop = True