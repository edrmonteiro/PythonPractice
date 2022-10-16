if __name__ == '__main__':
    S = ''
    Q = int(input())
    save = []
    for i in range(Q):
        o = input().split()
        if o[0] == '1':
            save.append(S)
            S = S + o[1]
        elif o[0] == '2':
            save.append(S)
            S = S[:-int(o[1])]
        elif o[0] == '3':
            index = int(o[1])
            print(S[index-1:index])
        elif o[0] == '4':
            S = save.pop()
        