"""
No Prefix Set
https://www.hackerrank.com/challenges/no-prefix-set/problem?h_r=next-challenge&h_v=zen

Given  strings. Each string contains only lowercase letters from (both inclusive). The set of  strings is said to be GOOD SET if no string is prefix of another string else, it is BAD SET. (If two strings are identical, they are considered prefixes of each other.)

For example, aab, abcde, aabcd is BAD SET because aab is prefix of aabcd.

Print GOOD SET if it satisfies the problem requirement.
Else, print BAD SET and the first string for which the condition fails.

Input Format
First line contains , the number of strings in the set.
Then next  lines follow, where  line contains  string.

Constraints

 Length of the string 

Output Format
Output GOOD SET if the set is valid.
Else, output BAD SET followed by the first string for which the condition fails.

Sample Input00

7
aab
defgab
abcde
aabcde
cedaaa
bbbbbbbbbb
jabjjjad
Sample Output00

BAD SET
aabcde
Sample Input01

4
aab
aac
aacghgh
aabghgh
Sample Output01

BAD SET
aacghgh
Explanation
aab is prefix of aabcde. So set is BAD SET and it fails at string aabcde.
"""

class Node:
    def __init__(self):
        self.children = [None] * 10 # from a to j
        self.isLeaf = False

def letterIndex(letter):
    return ord(letter) - ord('a')

def add(root, name):
    node = root
    existingTree = True
    for i in range(len(name)):
        index = letterIndex(name[i])
        if node.isLeaf: 
            return True
        if not node.children[index]:
            node.children[index] = Node()
            existingTree = False
        node = node.children[index]
    if existingTree:
        return True
    node.isLeaf = True
    return False

def solution(A):
    root = Node()
    for word in A:
        if add(root, word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")

# n = int(input())
# A = []
# for i in range(n):
#     A.append(input())
# solution(A)

A = ["aab","defgab","abcde","aabcde","cedaaa","bbbbbbbbbb","jabjjjad"]      # BAD SET   aabcde
solution(A)
A = ["aab","aac","aacghgh","aabghgh"]   # BAD Set   aacghgh
solution(A)
A = ["hgiiccfchbeadgebc","biiga","edchgb","ccfdbeajaeid","ijgbeecjbj","bcfbbacfbfcfbhcbfjafibfhffac","ebechbfhfcijcjbcehbgbdgbh","ijbfifdbfifaidje","acgffegiihcddcdfjhhgadfjb","ggbdfdhaffhghbdh","dcjaichjejgheiaie","d"]     # BAD Set   d
solution(A)

stop = True