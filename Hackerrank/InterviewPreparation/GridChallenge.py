def gridChallenge(grid):
    import copy
    # Write your code here
    for i, line in enumerate(grid):
        line1 = list(line)
        line1.sort()
        grid[i] = ''.join(line1)
    for i in range(len(grid[0])):
        column = [x[i] for x in grid]
        column_sorted = copy.deepcopy(column)
        column_sorted.sort()
        if column != column_sorted:

            return "NO"
    return "YES"






grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
gridChallenge(grid)


