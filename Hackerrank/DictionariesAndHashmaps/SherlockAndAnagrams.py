
"""
coding: utf-8
Created on 12/11/2020

@author: github.com/edrmonteiro

From: Hackerrank challenges
Language: Python
Title: Sherlock and Anagrams

Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example , the list of all anagrammatic pairs is  at positions  respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the number of anagrammatic pairs of substrings in .

sherlockAndAnagrams has the following parameter(s):

s: a string .
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a string  to analyze.

Constraints



String  contains only lowercase letters  ascii[a-z].

Output Format

For each query, return the number of unordered anagrammatic pairs.

Sample Input 0

2
abba
abcd
Sample Output 0

4
0
Explanation 0

The list of all anagrammatic pairs is  and  at positions  and  respectively.

No anagrammatic pairs exist in the second query as no character repeats.

Sample Input 1

2
ifailuhkqq
kkkk
Sample Output 1

3
10
Explanation 1

For the first query, we have anagram pairs  and  at positions  and  respectively.

For the second query:
There are 6 anagrams of the form  at positions  and .
There are 3 anagrams of the form  at positions  and .
There is 1 anagram of the form  at position .

Sample Input 2

1
cdcd
Sample Output 2

5
Explanation 2

There are two anagrammatic pairs of length :  and .
There are three anagrammatic pairs of length :  at positions  respectively.

"""


class wordClass:
    def __init__(self, word):
        self.width = len(word)
        self.totalSum = 0
        self.totalMultiplication = 1
        for letter in word:
            self.totalSum += ord(letter)
            self.totalMultiplication *= ord(letter)

def sherlockAndAnagrams(s):
    words = []
    for begin in range(len(s)):        
        for width in range(1, len(s) - begin + 1):
            words.append(wordClass(s[begin: begin + width]))
    words = sorted(words, key=lambda x: x.width)
    wordNumbers = []
    lastWidth = words[0].width
    anagrams = 0
    for word in words:
        wordNumber = str(word.totalSum) + str(word.totalMultiplication)
        if word.width == lastWidth:
            if wordNumber in wordNumbers:
                anagrams += wordNumbers.count(wordNumber)
                wordNumbers.append(wordNumber)
            else:
                wordNumbers.append(wordNumber)
        else:
            lastWidth = word.width
            wordNumbers = []
            wordNumbers.append(wordNumber)            
    return anagrams



s = 'abba'  #4
print(sherlockAndAnagrams(s))
s = 'abcd'  #0
print(sherlockAndAnagrams(s))
s = 'ifailuhkqq'    #3
print(sherlockAndAnagrams(s))
s = 'kkkk'      #10
print(sherlockAndAnagrams(s))
s = 'cdcd'  #5
print(sherlockAndAnagrams(s))
s = 'c'  #0
print(sherlockAndAnagrams(s))
s = 'cc'  #1
print(sherlockAndAnagrams(s))

s = 'ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel'  # 399
print(sherlockAndAnagrams(s))
s = 'gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde'  # 471
print(sherlockAndAnagrams(s))
s = 'mqmtjwxaaaxklheghvqcyhaaegtlyntxmoluqlzvuzgkwhkkfpwarkckansgabfclzgnumdrojexnrdunivxqjzfbzsodycnsnmw'  # 370
print(sherlockAndAnagrams(s))
s = 'ofeqjnqnxwidhbuxxhfwargwkikjqwyghpsygjxyrarcoacwnhxyqlrviikfuiuotifznqmzpjrxycnqktkryutpqvbgbgthfges'  # 403
print(sherlockAndAnagrams(s))
s = 'zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw'  # 428
print(sherlockAndAnagrams(s))


stop = True



# from collections import defaultdict
# def sherlockAndAnagrams(s):
#     d=defaultdict(int)
#     ans=0
#     for i in range(len(s)):
#         add=0
#         mul=1
#         for j in range(i,len(s)):
#             add+=ord(s[j])
#             mul=mul*ord(s[j])
#             check=(add,mul)
#             ans+=d[check]
#             d[check]+=1 
#     return ans
