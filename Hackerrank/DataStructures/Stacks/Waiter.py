"""
Hackerrank

Waiter
https://www.hackerrank.com/challenges/waiter/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

You are a waiter at a party. There are  stacked plates on pile . Each plate has a number written on it. Then there will be  iterations. In -th iteration, you start picking up the plates in  from the top one by one and check whether the number written on the plate is divisible by the -th prime. If the number is divisible, you stack that plate on pile . Otherwise, you stack that plate on pile . After  iterations, plates can only be on pile , . Output numbers on these plates from top to bottom of each piles in order of , .

Input Format

The first line contains two space separated integers,  and .
The next line contains  space separated integers representing the initial pile of plates, i.e., . The leftmost value represents the bottom plate of the pile.

Constraints




Output Format

Output  lines. Each line contains a number written on the plate. Printing should be done in the order defined above.

Sample Input 0

5 1
3 4 7 6 5
Sample Output 0

4
6
3
7
5
Explanation 0

Initially:

 = [3, 4, 7, 6, 5]<-TOP

After 1 iteration:

 = []<-TOP

 = [6, 4]<-TOP

 = [5, 7, 3]<-TOP

We should output numbers in  first from top to bottom, and then output numbers in  from top to bottom.

Sample Input 1

5 2
3 3 4 4 9
Sample Output 1

4
4
9
3
3
Explanation 1

Initially:

 = [3, 3, 4, 4, 9]<-TOP

After  iteration:

 = []<-TOP

 = [4, 4]<-TOP

 = [3, 3, 9]<-TOP

After  iteration:

 = []<-TOP

 = [4, 4]<- TOP

 = [3, 3, 9]<-TOP

We should output numbers in  first from top to bottom, and then output numbers in  from top to bottom.
"""

#!/bin/python3


def isPrime(number):
    i = 3
    while i**2 <= number :
        if number % i == 0:
            return False
        i += 2
    return True

def getPrimes(qtd):
    i = 1
    primes = [2]
    divisor = 3
    while i < qtd:
        if isPrime(divisor):
           primes.append(divisor)
           i += 1
        divisor += 2
    return(primes)

def waiter(number, q):
    primes = getPrimes(q)
    answer = []
    for i in range(q):
        A = []
        for item in number:
            if item % primes[i] == 0:
                answer.append(item)
            else:
                A.append(item)
        A.reverse()
        number = A 
    while A:
        answer.append(A.pop())
    return answer

q = 1
number = [3, 4, 7, 6, 5]    # [4, 6, 3, 7, 5]
print(waiter(number, q))

q = 2
number = [3, 3, 4, 4, 9]    # [4, 4, 9, 3, 3]
print(waiter(number, q))

q = 21
number = [80, 37, 86, 79, 8, 39, 43, 41, 15, 33, 30, 15, 45, 55, 61, 74, 49, 49, 20, 66, 77, 19, 85, 44, 81, 82, 27, 5, 36, 83, 91, 45, 39, 44, 19, 44, 71, 49, 8, 66, 81, 40, 29, 60, 35, 31, 44]
print(waiter(number, q))    # [80,86,8,30,74,20,66,44,82,36,44,44,8,66,40,60,44,81,39,45,27,81,45,15,33,15,39,55,85,5,35,49,91,77,49,49,19,19,29,31,37,41,43,61,71,79,83]

stop = True

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nq = input().split()

#     n = int(nq[0])

#     q = int(nq[1])

#     number = list(map(int, input().rstrip().split()))

#     result = waiter(number, q)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

