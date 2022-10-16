def cookies(k, A):
    import heapq
    # Write your code here
    heapq.heapify(A)
    count = 0
    try:
        a = heapq.heappop(A)
        while a < k:
            b = heapq.heappop(A)
            heapq.heappush(A, a+2*b)
            count +=1
            a = heapq.heappop(A)
        return count
    except:
        return -1
    
            
k = 9
A =[2,7,3,6,4,6]

k = 10
A =[1,1,1]

k = 3581    #7
A = [6214, 8543, 9266, 1150, 7498, 7209, 9398, 1529, 1032, 7384, 6784, 34, 1449, 7598, 8795, 756, 7803, 4112, 298, 4967, 1261, 1724, 4272, 1100, 9373]
print(cookies(k, A))