"""
12. Print balanced brace combinations
Print all braces combinations for a given value n so that they are balanced. For this solution, we will be using recursion. 
"""
import copy
def print_all_braces_rec(n, left_count, right_count, output, result):
 
  if left_count >= n and right_count >= n:
    result.append(copy.copy(output))
    
  if left_count < n:
    output += '{'
    print_all_braces_rec(n, left_count + 1, right_count, output, result)
    output.pop()
 
  if right_count < left_count:
    output += '}'
    print_all_braces_rec(n, left_count, right_count + 1, output, result)
    output.pop()
 
def print_all_braces(n):
  output = []
  result = []
  print_all_braces_rec(n, 0, 0, output, result)
  return result
 
result = print_all_braces(3)
 
for rs in result: 
  print(rs)

stop = True

"""
Runtime Complexity: Exponential, 2^n​​
Memory Complexity: Linear, O(n)
The solution is to maintain counts of left_braces and right_braces. The basic algorithm is as follows:​
left_braces count: 0
right_braces count: 0
 
if left_braces count is less than n:
  add left_braces and recurse further
if right_braces count is less than left_braces count:
  add right_braces and recurse further
stop recursing when left_braces and right_braces counts are both equal to n

"""

stop = True