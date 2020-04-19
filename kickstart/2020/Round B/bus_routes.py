T = int(input())

for t in range(1,T+1):
    N,D = list(map(int,input().split()))
    X = list(map(int,input().split()))
    
    i = N-1
    while (i >= 0):
        #print(X[i], D)
        if D % X[i] == 0:
            i -= 1
        else:
            D -= (D % X[i])
    
    print("Case #{}: {}".format(t,D))
