

def flippingMatrix(matrix):
    # Size of Upper left Quadrant is n * n
    n = len(matrix) // 2
    Result = 0
    for row in range(n):
        for column in range(n):
            quadrant1 = matrix[row][len(matrix[0]) - column - 1]
            quadrant2 = matrix[row][column]
            quadrant3 = matrix[len(matrix) - row - 1][column]
            quadrant4 = matrix[len(matrix) - row - 1][len(matrix[0]) - column - 1]
            Result += max(quadrant1, quadrant2, quadrant3, quadrant4)
    return Result


matrix = [[1,2],[3,4]]
#4
print(flippingMatrix(matrix))

matrix  =  [[112,42,114,119],[56,125,101,49],[15,78,56,43],[62,98,83,108]]
# 119  + 114  + 56 + 125 = 414
print(flippingMatrix(matrix))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()