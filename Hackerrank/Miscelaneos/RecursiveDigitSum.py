def superDigit(n, k):
    # Write your code here
    #n = n*k
    n = str(sum([int(x) for x in n])*k)
    while len(n)>1:
        n = str(sum([int(x) for x in n]))
    return int(n)

n = '148'
k = 3
print(superDigit(n, k))

print("end")