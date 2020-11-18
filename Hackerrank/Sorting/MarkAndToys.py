"""coding: utf-8
Created on 18/11/2020

@author: github.com/edrmonteiro
From: Hackerrank challenges
Language: Python
Title: Sorting: Mark And Toys

Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.

Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if  and Mark has  to spend, he can buy items  for , or  for  units of currency. He would choose the first group of  items.

Function Description

Complete the function maximumToys in the editor below. It should return an integer representing the maximum number of toys Mark can purchase.

maximumToys has the following parameter(s):

prices: an array of integers representing toy prices
k: an integer, Mark's budget
Input Format

The first line contains two integers,  and , the number of priced toys and the amount Mark has to spend.
The next line contains  space-separated integers 

Constraints




A toy can't be bought multiple times.

Output Format

An integer that denotes the maximum number of toys Mark can buy for his son.

Sample Input

7 50
1 12 5 111 200 1000 10
Sample Output

4
Explanation

He can buy only  toys at most. These toys have the following prices: 

"""


def maximumToys(prices, k):
    prices.sort()
    total = 0
    for i in range(len(prices)):
        if total + prices[i] <= k:
            total += prices[i]
        else:
            return i
    return len(prices)


prices = [1, 2, 3, 4]
k = 7
print(maximumToys(prices, k))

prices = [1]
k = 7
print(maximumToys(prices, k))

prices = []
k = 7
print(maximumToys(prices, k))

prices = [1]
k = 0
print(maximumToys(prices, k))

stop = True