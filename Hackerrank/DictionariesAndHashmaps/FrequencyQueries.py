"""
coding: utf-8
Created on 14/11/2020

@author: github.com/edrmonteiro

From: Hackerrank challenges
Language: Python
Title: Frequency Queries

You are given  queries. Each query is of the form two integers described below:
-  : Insert x in your data structure.
-  : Delete one occurence of y from your data structure, if present.
-  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element. For example, you are given array . The results of each operation are:

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
Return an array with the output: .

Function Description

Complete the freqQuery function in the editor below. It must return an array of integers where each element is a  if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.

freqQuery has the following parameter(s):

queries: a 2-d array of integers
Input Format

The first line contains of an integer , the number of queries.
Each of the next  lines contains two integers denoting the 2-d array .

Constraints

All 
Output Format

Return an integer array consisting of all the outputs of queries of type .

Sample Input 0

8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
Sample Output 0

0
1
Explanation 0

For the first query of type , there is no integer whose frequency is  (). So answer is .
For the second query of type , there are two integers in  whose frequency is  (integers =  and ). So, the answer is .

Sample Input 1

4
3 4
2 1003
1 16
3 1
Sample Output 1

0
1
Explanation 1

For the first query of type , there is no integer of frequency . The answer is . For the second query of type , there is one integer,  of frequency  so the answer is .

Sample Input 2

10
1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2
Sample Output 2

0
1
1
Explanation 2

When the first output query is run, the array is empty. We insert two 's and two 's before the second output query,  so there are two instances of elements occurring twice. We delete a  and run the same query. Now only the instances of  satisfy the query.

"""

# def freqQuery(queries):
#     results = []
#     lookup = dict()
#     freqs = defaultdict(set)
#     for command, value in queries:
#         freq = lookup.get(value, 0)
#         if command == 1:
#             lookup[value] = freq + 1
#             freqs[freq].discard(value)
#             freqs[freq + 1].add(value)
#         elif command == 2:
#             lookup[value] = max(0, freq - 1)
#             freqs[freq].discard(value)
#             freqs[freq - 1].add(value)
#         elif command == 3:
#             results.append(1 if freqs[value] else 0)
# #     return results  

def freqQuery(queries):
    freq = Counter()
    cnt = Counter()
    arr = []
    for q in queries:
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1

        elif q[0]==2:
            if freq[q[1]]>0:
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1
        else:
            if cnt[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)
    return arr


# def freqQuery(queries):
#     stack = {}
#     valuesStack = []
#     answer = []
#     for query in queries:
#         if query[0] == 1:            
#             stack[query[1]] = stack.get(query[1], 0) + 1
#             try:
#                 itemValue = stack.get(query[1], 0)
#                 valuesStack.remove(itemValue - 1)
#             except:
#                 pass
#             valuesStack.append(itemValue)
#         elif query[0] == 2:            
#             stack[query[1]] = max(stack.get(query[1], 0) - 1, 0)
#             try:
#                 itemValue = stack.get(query[1], 0)
#                 valuesStack.remove(itemValue + 1)
#             except:
#                 pass
#             valuesStack.append(itemValue)
#         elif query[0] == 3:
#             try:
#                 valuesStack.index(query[1])
#                 answer.append(1)
#             except:
#                 answer.append(0)
#     return answer

# def freqQuery(queries):
#     stack = {}
#     answer = []
#     for query in queries:
#         if query[0] == 1:
#             stack[query[1]] = stack.get(query[1], 0) + 1
#         elif query[0] == 2:
#             stack[query[1]] = max(stack.get(query[1], 0) - 1, 0)
#         elif query[0] == 3:
#             exists = False
#             for key, value in stack.items():
#                 if value == query[1]:
#                     exists = True
#             if exists:
#                 answer.append(1)
#             else:
#                 answer.append(0)
#     return answer
        


queries = [[1, 5], [1, 6],[3, 2],[1, 10],[1, 10],[1, 6],[2, 5],[3, 2]]
print(freqQuery(queries))

queries = [[3, 4],[2, 1003],[1, 16],[3, 1]]
print(freqQuery(queries))

queries = [[3, 4],[2, 1003],[1, 16],[3, 1]]
print(freqQuery(queries))

queries = [[1, 3],[2, 3],[3, 2],[1, 4],[1, 5],[1, 5],[1, 4],[3, 2],[2, 4],[3, 2]]
print(freqQuery(queries))



stop = True