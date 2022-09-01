def minimumBribes(q):
    bribe = 0
    min_val = len(q)
    for i in range(len(q)-1, -1, -1):
        if q[i]-(i+1) > 2:
            print('Too chaotic')
            return
        if q[i] > i+1:
            bribe+=q[i]-i-1
        else:
            if q[i] < min_val:
                min_val = q[i]
            elif q[i] > min_val:
                bribe+=1
    print(bribe)

q = [3,2,1]
#q = [2, 1, 5, 3, 4]
# q = [2, 5, 1, 3, 4]
q = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(q)