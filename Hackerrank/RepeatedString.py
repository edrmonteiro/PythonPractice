"""
coding: utf-8
Created on 09/11/2020

@author: github.com/edrmonteiro

From: Hackerrank challenges
Language: Python
Title: Repeated String

Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .

Constraints

For  of the test cases, .
Output Format

Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

Sample Input 0

aba
10
Sample Output 0

7
Explanation 0
The first  letters of the infinite string are abaabaabaa. Because there are  a's, we print  on a new line.

Sample Input 1

a
1000000000000
Sample Output 1

1000000000000
Explanation 1
Because all of the first  letters of the infinite string are a, we print  on a new line.

"""

def repeatedString(s, n):
    count = s.count('a')
    multiply = (n // len(s))
    count *= multiply
    residual = n - (len(s) * multiply)
    if residual > 0:
        count += s[:residual].count('a')

    return count

s = "a"
n = 1000000000000
print(repeatedString(s, n))

s = "abcac"
n = 10
print(repeatedString(s, n))

s = "abca"
n = 10
print(repeatedString(s, n))

s = "aba"
n = 10
print(repeatedString(s, n))



stop = True