#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class TrieNode():
    def __init__(self):
        self.is_word = False
        self.children = {}   
def addAndSearch(root: TrieNode, word: str) -> bool:
    cur = root
    
    for ch in word:
        if ch not in cur.children:
            cur.children[ch] = TrieNode()
        cur = cur.children[ch]
        
        # Current node is marked end of word by a previous word
        if cur.is_word:
            return True
    
    # Handles case of aabcd coming before aab, aab is a bad prefix
    for i in range(ord('j')):
        char = chr(i + ord('a'))
        if char in cur.children:
            return True
    
    cur.is_word = True
    return False

def noPrefix(words):
    # Write your code here
    root = TrieNode()
    
    for word in words:
        if addAndSearch(root, word):
            print("BAD SET")
            print(word)
            return
    
    print("GOOD SET")
    return

# words =["aab","aac","aacghgh","aabghgh"]
# print(noPrefix(words))

words =["aabghgh","aab","aac","aacghgh"]
print(noPrefix(words))

words = ["hgiiccfchbeadgebc","biiga","edchgb","ccfdbeajaeid","ijgbeecjbj","bcfbbacfbfcfbhcbfjafibfhffac","ebechbfhfcijcjbcehbgbdgbh","ijbfifdbfifaidje","acgffegiihcddcdfjhhgadfjb","ggbdfdhaffhghbdh","dcjaichjejgheiaie","d","jeedfch","ahabicdffbedcbdeceed","fehgdfhdiffhegafaaaiijceijdgbb","beieebbjdgdhfjhj","ehg","fdhiibhcbecddgijdb"]   
print(noPrefix(words))

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)