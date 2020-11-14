"""
coding: utf-8
Created on 13/11/2020

@author: github.com/edrmonteiro

From: Hackerrank challenges
Language: Python
Title: Count Triplets

You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .

For example, . If , we have  and  at indices  and .

Function Description

Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given  as an integer.

countTriplets has the following parameter(s):

arr: an array of integers
r: an integer, the common ratio
Input Format

The first line contains two space-separated integers  and , the size of  and the common ratio.
The next line contains  space-seperated integers .

Constraints

Output Format

Return the count of triplets that form a geometric progression.

Sample Input 0

4 2
1 2 2 4
Sample Output 0

2
Explanation 0

There are  triplets in satisfying our criteria, whose indices are  and 

Sample Input 1

6 3
1 3 9 9 27 81
Sample Output 1

6
Explanation 1

The triplets satisfying are index , , , ,  and .

Sample Input 2

5 5
1 5 5 25 125
Sample Output 2

4
Explanation 2

The triplets satisfying are index , , , .

"""


# Complete the countTriplets function below.

def countTriplets(arr, r):
        triplets = 0
        mult2 = {}
        mult1 = {}
        for item in reversed(arr):
            if item * r in mult1:
                triplets += mult1[item * r]
            if item * r in mult2:
                mult1[item] = mult1.get(item, 0) + mult2[item * r]
            mult2[item] = mult2.get(item, 0) + 1
        return triplets


arr = [1, 2, 2, 4] #2
r = 2
print(countTriplets(arr, r))

arr = [1,3,9,9,27,81] #6
r = 3
print(countTriplets(arr, r))

arr = [1, 5, 5, 25, 125] #4
r = 5
print(countTriplets(arr, r))

stop = True