"""
Maximum Element
You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Input Format

The first line of input contains an integer, . The next  lines each contain an above mentioned query. (It is guaranteed that each query is valid.)

Constraints



Output Format

For each type  query, print the maximum element in the stack on a new line.

Sample Input

10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91

"""


#def main(queries):
def main():
    def solution(query):
        command = query[0]
        if command == 1:
            stack.append(max(query[1], stack[-1]))
        elif command == 2:
            if stack:
                stack.pop(-1)
        elif command == 3:
            if stack:
                print(stack[-1])

    stack = [0]
    # if queries:
    #     for query in queries:
    #         solution(query)

    n = int(input())
    
    for _ in range(n):
        query = list(map(int, input().strip().split()))
        solution(query)


A = [[1, 1],[1, 44],[3,],[3,],[2,],[3,],[3,],[1, 3],[1, 37],[2,],[3,],[1, 29],[3,],[1, 73],[1, 51],[3,],[3,],[3,],[1, 70],[3,],[1, 8],[2,],[1, 49],[1, 56],[1, 81],[2,],[1, 59],[1, 44],[2,],[3,],[3,],[2,],[3,],[3,],[1, 4],[3,],[1, 89],[2,],[1, 37],[1, 50],[1, 64],[2,],[1, 49],[1, 35],[1, 85],[3,],[1, 41],[2,],[3,],[3,],[1, 86],[3,],[1, 60],[1, 8],[3,],[1, 100],[3,],[1, 83],[3,],[1, 47],[2,],[1, 78],[2,],[1, 55],[1, 97],[2,],[3,],[1, 40]]
#main(A)
main()


stop = True



