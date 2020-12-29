"""
Largest Rectangle
https://www.hackerrank.com/challenges/largest-rectangle/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by . If you join  adjacent buildings, they will form a solid rectangle of area .

For example, the heights array . A rectangle of height  and length  can be constructed within the boundaries. The area formed is .

Function Description

Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

largestRectangle has the following parameter(s):

h: an array of integers representing building heights
Input Format

The first line contains , the number of buildings.
The second line contains  space-separated integers, each representing the height of a building.

Constraints

Output Format

Print a long integer representing the maximum area of rectangle formed.

Sample Input

5
1 2 3 4 5
Sample Output

9
Explanation

An illustration of the test case follows.
"""

def largestRectangle(h):
    def down():
        last = stack.pop()
        if stack:
            width = i - stack[-1] - 1
        else:
            width = i
        return h[last] * width
    
    stack = []
    area = 0
    i = 0
    while i < len(h):
        if not stack or h[stack[-1]] <= h[i]:
            stack.append(i)
            i += 1           
        else:
            area = max(area, down())

    while stack:
        area = max(area, down())
        
    return area



h = [3, 2, 3]     # 6
print(largestRectangle(h))

h = [1, 2, 3, 4, 5]     # 9
print(largestRectangle(h))

h = [1, 3, 5, 9, 11]    #18
print(largestRectangle(h))

h = [11, 11, 10, 10, 10]    #50
print(largestRectangle(h))

h = [5, 4, 3, 2, 1]     # 9
print(largestRectangle(h))

stop = True
