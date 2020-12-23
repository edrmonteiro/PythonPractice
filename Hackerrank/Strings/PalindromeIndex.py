"""
Palindrome Index
https://www.hackerrank.com/challenges/palindrome-index/problem?h_r=next-challenge&h_v=zen

Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

Example

Either remove 'b' at index  or 'c' at index .

Function Description

Complete the palindromeIndex function in the editor below.

palindromeIndex has the following parameter(s):

string s: a string to analyze
Returns

int: the index of the character to remove or 
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a query string .

Constraints

All characters are in the range ascii[a-z].
Sample Input

STDIN   Function
-----   --------
3       q = 3
aaab    s = 'aaab' (first query)
baa     s = 'baa'  (second query)
aaa     s = 'aaa'  (third query)
Sample Output

3
0
-1
Explanation

Query 1: "aaab"
Removing 'b' at index  results in a palindrome, so return .

Query 2: "baa"
Removing 'b' at index  results in a palindrome, so return .

Query 3: "aaa"
This string is already a palindrome, so return . Removing any one of the characters would result in a palindrome, but this test comes first.

Note: The custom checker logic for this challenge is available here.

"""

def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i - 1]:
            return False
    return True

def palindromeIndex1(s):
    if isPalindrome(s):
        return -1
    for i in range(len(s)):
        if isPalindrome(s[:i] + s[i + 1:]):
            return i
    return -1

# error
def palindromeIndex2(s):
    a = 0
    b = len(s) - 1
    eliminated = -1
    while a < (len(s) // 2) + 1:
        if s[a] != s[b]:
            if s[a + 1] != s[b]:
                if s[a] != s[b - 1]:
                    return -1
                else:
                    if eliminated != -1:
                        return -1
                    eliminated = b
                    b -= 1
            else:
                if eliminated != -1:
                        return -1
                eliminated = a
                a += 1
        a += 1
        b -= 1
        

    return eliminated

def find_mismatching_pair(s):
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return i, j    
    
def is_palindrome(s):
    i, j = find_mismatching_pair(s)
    return j <= i
    
    
def palindromeIndex(s):
    i, j = find_mismatching_pair(s)
    return -1 if j <= i else i if is_palindrome(s[i+1 : j+1]) else j

s = "hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"
print(palindromeIndex(s))   # 44

s = "ab"
print(palindromeIndex(s))   # 0

s = "a"
print(palindromeIndex(s))   # -1

s = "bcbc"
print(palindromeIndex(s))   # 0

s = 'aaab'
print(palindromeIndex(s))   # 3

s = 'baa' 
print(palindromeIndex(s))   # 0

s = 'aaa' 
print(palindromeIndex(s))   # -1

stop = True
