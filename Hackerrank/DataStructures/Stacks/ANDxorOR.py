"""
Hackerrank
AND xor OR
https://www.hackerrank.com/challenges/and-xor-or/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

Given an array  of  distinct elements. Let  and  be the smallest and the next smallest element in the interval  where .
.
where , are the bitwise operators ,  and  respectively.
Your task is to find the maximum possible value of .

Input Format

First line contains integer .
Second line contains  integers, representing elements of the array .
Constraints
Output Format
Print the value of maximum possible value of .
Sample Input
5
9 6 3 5 2
Sample Output

15
Explanation

Consider the interval  the result will be maximum.

"""

def andXorOr(A):
    maximum = 0
    stack = []
    for m1 in A:
        while stack:
            m2 = stack[-1]
            s = (((m1 & m2) ^ (m1 | m2)) & (m1 ^ m2))
            maximum = max(maximum,  s)
            if m1 < m2:
                stack.pop()
            else:
                break
        stack.append(m1)
    return maximum

# a = [9, 6, 3, 5, 2]
# a = [9, 8, 3, 5, 7]
# #a = [5, 6, 7, 8, 4]
# print(andXorOr1(a))
# print(andXorOr(a))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a_count = int(input())
    a = list(map(int, input().rstrip().split()))
    result = andXorOr(a)
    fptr.write(str(result) + '\n')
    fptr.close()