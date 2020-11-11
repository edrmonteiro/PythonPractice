"""
coding: utf-8
Created on 10/11/2020

@author: github.com/edrmonteiro

From: Hackerrank challenges
Language: Python
Title: Arrays: Left Rotation

A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

An array of integers .
An integer , the number of rotations.
Input Format

The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
The second line contains  space-separated integers .

Constraints

Output Format

Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
Explanation

When we perform  left rotations, the array undergoes the following sequence of changes:

"""

def rotLeft(a, d):
    b = [None] * len(a)
    shift = d
    for i in range(len(a)):
        index = (i + shift) % len(a)
        b[i] = a[index]
    return b


a = [1,2,3,4,5]
d = 2
print(rotLeft(a, d))

a = [1,2,3,4,5]
d = 4
print(rotLeft(a, d))

stop = True