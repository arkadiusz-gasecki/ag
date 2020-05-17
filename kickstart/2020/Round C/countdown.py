T = int(input())


for t in range(1,T+1):
    N,K = map(int,input().split())

    A = list(map(int,input().split()))
    

    countdowns = 0
    i = 0
    while i < N:
        if A[i] == K:
            
            if i+K > N:
                break
            
            is_cnt = True
            for j in range(i,i+K-1):
                if A[j] != A[j + 1]+1:
                    is_cnt = False
                    i = j
            if is_cnt:
                countdowns += 1
                i += (K-1)
        i += 1

    print("Case #{}: {}".format(t,countdowns))           
