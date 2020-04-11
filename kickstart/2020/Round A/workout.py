#only test set 1


T = int(input())

for t in range(1,T+1):
    N, K = map(int, input().split())
    M = list(map(int, input().split()))
    
    differences = list()
    for i in range(0,len(M)-1):
        differences.append(M[i+1] - M[i])
    
    differences.sort(reverse=True)
    
    if (len(differences) < 2):
        answer = (differences[0]+1) // 2
    else:
        answer = max((differences[0]+1) // 2, differences[1])
    
    print("Case #{}: {}".format(t,answer))
