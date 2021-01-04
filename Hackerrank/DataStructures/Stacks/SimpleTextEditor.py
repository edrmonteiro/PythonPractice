"""
Simple Text Editor
https://www.hackerrank.com/challenges/simple-text-editor/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen

In this challenge, you must implement a simple text editor. Initially, your editor contains an empty string, . You must perform  operations of the following  types:

append - Append string  to the end of .
delete - Delete the last  characters of .
print - Print the  character of .
undo - Undo the last (not previously undone) operation of type  or , reverting  to the state it was in prior to that operation.
Input Format

The first line contains an integer, , denoting the number of operations.
Each line  of the  subsequent lines (where ) defines an operation to be performed. Each operation starts with a single integer,  (where ), denoting a type of operation as defined in the Problem Statement above. If the operation requires an argument,  is followed by its space-separated argument. For example, if  and , line  will be 1 abcd.

Constraints

The sum of the lengths of all  in the input .
The sum of  over all delete operations .
All input characters are lowercase English letters.
It is guaranteed that the sequence of operations given as input is possible to perform.
Output Format

Each operation of type  must print the  character on a new line.

Sample Input

8
1 abc
3 3
2 3
1 xy
3 2
4 
4 
3 1
Sample Output

c
y
a
Explanation

Initially,  is empty. The following sequence of  operations are described below:

. We append  to , so .
Print the  character on a new line. Currently, the  character is c.
Delete the last  characters in  (), so .
Append  to , so .
Print the  character on a new line. Currently, the  character is y.
Undo the last update to , making  empty again (i.e., ).
Undo the next to last update to  (the deletion of the last  characters), making .
Print the  character on a new line. Currently, the  character is a.


"""

Q = int(input())
entries = []

for _ in range(Q):
    entry = input().split()
    func = int(entry[0])
    value = entry[1] if len(entry) > 1 else None
    entries.append([func, value])
#entries = [[1, "abc"],[3, 3],[2, 3],[1, "xy"],[3, 2],[4],[4],[3, 1]]

S = ""
stack = []
for entry in entries:    
    if entry[0] == 1:
        stack.append(S)
        S += entry[1]
    elif entry[0] == 2:
        stack.append(S)
        S = S[:-int(entry[1])]
    elif entry[0] == 3:
        print (S[int(entry[1]) - 1])
    elif entry[0] == 4:
        S = stack.pop()
    
    

stop = True