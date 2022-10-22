def truckTour(petrolpumps):
    # Write your code here
    autonomy = []
    total = 0
    start = 0
    print(petrolpumps)
    for i,step in enumerate(petrolpumps):
        stage = step[0] - step[1]
        autonomy.append(stage)

        if total < 0:
            start = i
        if stage + total > 0:
            total += stage
        else:
            total += stage
            while len(autonomy) > start  and total<0:
                total -= autonomy[start]
                start += 1
                #total = sum(autonomy[start:])
    return start

petrolpumps = [[1, 5], [10, 3], [3, 4]]   #1
print(truckTour(petrolpumps))



 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
