"""
Poisonous Plants
https://www.hackerrank.com/challenges/poisonous-plants/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

There are a number of plants in a garden. Each of the plants has been treated with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.

You are given the initial values of the pesticide in each of the plants. Determine the number of days after which no plant dies, i.e. the time after which there is no plant with more pesticide content than the plant to its left.

Example

 // pesticide levels

Use a -indexed array. On day , plants  and  die leaving . On day , plant  in  dies leaving . There is no plant with a higher concentration of pesticide than the one to its left, so plants stop dying after day .

Function Description
Complete the function poisonousPlants in the editor below.

poisonousPlants has the following parameter(s):

int p[n]: the pesticide levels in each plant
Returns
- int: the number of days until plants no longer die from pesticide

Input Format

The first line contains an integer , the size of the array .
The next line contains  space-separated integers .

Constraints



Sample Input

7
6 5 8 4 7 10 9
Sample Output

2
Explanation

Initially all plants are alive.

Plants = {(6,1), (5,2), (8,3), (4,4), (7,5), (10,6), (9,7)}

Plants[k] = (i,j) => jth plant has pesticide amount = i.

After the 1st day, 4 plants remain as plants 3, 5, and 6 die.

Plants = {(6,1), (5,2), (4,4), (9,7)}

After the 2nd day, 3 plants survive as plant 7 dies.

Plants = {(6,1), (5,2), (4,4)}

Plants stop dying after the 2nd day.

"""

def poisonousPlants(pop):
    stack = []
    maxdays = 0
    for item in p:
        days = 1
        while stack and stack[-1][0] >= item:
            day = stack.pop()[1]
            days = max(days, day + 1)        
        if not stack:
            days = 0        
        maxdays = max(maxdays, days)
        stack.append((item, days))    
    return maxdays

p = [6, 5, 8, 4, 7, 10, 9]
print(poisonousPlants(p))
stop = True