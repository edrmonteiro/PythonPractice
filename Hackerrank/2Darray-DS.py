"""
coding: utf-8
Created on 10/11/2020

@author: github.com/edrmonteiro

From: Hackerrank challenges
Language: Python
Title: 2D array - DS

Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

Example


-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18
The highest hourglass sum is  from the hourglass beginning at row , column :

0 4 3
  1
8 6 6
Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

int arr[6][6]: an array of integers
Returns

int: the maximum hourglass sum
Input Format

Each of the  lines of inputs  contains  space-separated integers .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

 contains the following hourglasses:

image

The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4

"""
def hourglassSum(arr):
    maximumHourGlass = sum(arr[0][0 : 3]) + arr[1][1] + sum(arr[2][0 : 3])
    currentHourGlass = 0
    for i in range(0,4):
        for j in range(0,4):
            line1 = sum(arr[i][j : j + 3]) 
            line2 = arr[i + 1][j + 1] 
            line3 =sum(arr[i + 2][j : j + 3])
            currentHourGlass = line1 + line2 + line3
            maximumHourGlass = max(maximumHourGlass, currentHourGlass)
    return maximumHourGlass 

arr = [                        \
[-9,-9, -9, 1, 1, 1],          \
[ 0,-9,  0, 4, 3, 2],          \
[-9,-9, -9, 1, 2, 3],          \
[ 0, 0,  8, 6, 6, 0],          \
[ 0, 0,  0,-2, 0, 0],          \
[ 0, 0,  1, 2, 4, 0]           \
]

print(hourglassSum(arr))

arr = [  
[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]
print(hourglassSum(arr))

stop = True