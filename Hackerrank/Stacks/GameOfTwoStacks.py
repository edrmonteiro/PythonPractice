"""
Game of Two Stacks
https://www.hackerrank.com/challenges/game-of-two-stacks/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
Alexa has two stacks of non-negative integers, stack  and stack  where index  denotes the top of the stack. Alexa challenges Nick to play the following game:

In each move, Nick can remove one integer from the top of either stack  or stack .
Nick keeps a running sum of the integers he removes from the two stacks.
Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer  given at the beginning of the game.
Nick's final score is the total number of integers he has removed from the two stacks.
Given , , and  for  games, find the maximum possible score Nick can achieve (i.e., the maximum number of integers he can remove without being disqualified) during each game and print it on a new line.

Input Format

The first line contains an integer,  (the number of games). The  subsequent lines describe each game in the following format:

The first line contains three space-separated integers describing the respective values of  (the number of integers in stack ),  (the number of integers in stack ), and  (the number that the sum of the integers removed from the two stacks cannot exceed).
The second line contains  space-separated integers describing the respective values of .
The third line contains  space-separated integers describing the respective values of .
Constraints

Subtasks

 for  of the maximum score.
Output Format

For each of the  games, print an integer on a new line denoting the maximum possible score Nick can achieve without being disqualified.

Sample Input 0

1
5 4 10
4 2 4 6 1
2 1 8 5
Sample Output 0

4
Explanation 0

The two stacks initially look like this:

image

The image below depicts the integers Nick should choose to remove from the stacks. We print  as our answer, because that is the maximum number of integers that can be removed from the two stacks without the sum exceeding .

image

(There can be multiple ways to remove the integers from the stack, the image shows just one of them.)

"""

#ok
def twoStacks(x, a, b):
    a.reverse()
    b.reverse()
    stack = []
    total, count = 0, 0

    while a:
        number = a.pop()
        if (total + number) <= x:
            total += number
            count += 1
            stack.append(number)
        else: break
    
    maxCount = count

    while b:
        number = b.pop()
        total += number
        count += 1
        while total > x and stack:
            total -= stack.pop()
            count -= 1
        if total <= x and count > maxCount: 
            maxCount = count
    
    return maxCount

#Timout error
def twoStacks1(x, a, b):
    stack = []
    total, count = 0, 0

    while a:
        number = a.pop(0)
        if total + number > x:
            break
        total += number
        count += 1
        stack.append(number)
    
    maxCount = count

    while b:
        number = b.pop(0)
        total += number
        count += 1
        while total > x and stack:
            total -= stack.pop()
            count -= 1
        maxCount = max(maxCount, count)
        if total <= x and count > maxCount: 
            maxCount = count
    
    return maxCount


x = 10
a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]
print(twoStacks1(x, a, b)) #4

x = 12
a = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0]
b = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
print(twoStacks1(x, a, b)) #32


x = 62
a = [7, 15, 12, 0, 5, 18, 17, 2, 10, 15, 4, 2, 9, 15, 13, 12, 16]
b = [12, 16, 6, 8, 16, 15, 18, 3, 11, 0, 17, 7, 6, 11, 14, 13, 15, 6, 18, 6, 16, 12, 16, 11, 16, 11]
print(twoStacks(x, a, b)) #6

x = 55
a = [11, 6, 1, 13, 14, 7, 8, 10, 3, 17, 7, 18, 6, 4, 5, 13, 17, 4, 16, 9, 17, 16, 12, 6, 7]
b = [10, 15, 13, 17, 10, 7, 0, 16, 8, 13, 11, 8, 14, 13]
print(twoStacks(x, a, b)) #6

x = 0
a = [4, 2]
b = [2]
print(twoStacks(x, a, b)) #0

x = 2
a = []
b = []
print(twoStacks(x, a, b)) #0

stop = True