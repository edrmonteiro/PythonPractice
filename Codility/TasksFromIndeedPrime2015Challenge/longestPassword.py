"""
coding: utf-8
Created on 29/10/2020

@author: github.com/eduardormonteiro

From: Codility Lessons
"""

# LongestPassword
# You would like to set a password for a bank account. However, there are three restrictions on the format of the password:
# it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
# there should be an even number of letters;
# there should be an odd number of digits.
# You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces. The goal is to choose the longest word that is a valid password. You can assume that if there are K spaces in string S then there are exactly K + 1 words.

# For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007". Thus the longest password is "pass007" and its length is 7. Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).

# Write a function:

# def solution(S)

# that, given a non-empty string S consisting of N characters, returns the length of the longest word from the string that is a valid password. If there is no such word, your function should return −1.

# For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as explained above.

# Assume that:

# N is an integer within the range [1..200];
# string S consists only of printable ASCII characters and spaces.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

class passwordClass(object):
    def __init__(self, password):
        self.password = password
        self.valid = True
        self.qtdLetters = 0
        self.qtdNumbers = 0
        self.Len = 0
        passwordClass.fillItems(self)
        passwordClass.isValid(self)

    def fillItems(self):
        for i, char in enumerate(self.password):
            digit = ord(char)
            if digit >= 48 and digit <= 57:
                self.qtdNumbers += 1            
                self.Len += 1            
            elif digit >= 65 and digit <= 90:
                self.qtdLetters += 1
                self.Len += 1
            elif digit >= 97 and digit <= 122:
                self.qtdLetters += 1
                self.Len += 1
            else:
                self.valid = False
                return
    def isValid(self):
        if self.qtdLetters % 2 != 0:
            self.valid = False
        if self.qtdNumbers % 2 == 0:
            self.valid = False

def solution(S):
    passwords =[]
    for item in S.split():
        password = passwordClass(item)
        if password.valid:
            passwords.append(password)
    passwords = sorted(passwords, key=lambda x: x.Len, reverse=True)
    if len(passwords) > 0:
        return passwords[0].Len
    else:
        return -1


# S = "test 5 a0A pass007 ?xy1"
# print(solution(S))


S = "t"
print(solution(S))

stop = True
