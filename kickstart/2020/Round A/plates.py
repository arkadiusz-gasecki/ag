T = int(input())

for t in range(1,T+1):
    N,K,P = map(int,input().split())
    S = list()
    for i in range(0,N):
        Si = list(map(int,input().split()))
        S.append(Si)

    all_stacks = list()
    for stack in S:
        stack_val = list()
        prev_sum = 0
        stack_val.append(0)
        for i,elem in enumerate(stack):
            stack_val.append(elem+prev_sum)
            prev_sum += elem
        all_stacks.append(stack_val)
    
    dp = [[ 0 for i in range(0,P+1)] for j in range(0,N+1)]
    
    for i in range(1,N+1):
        for j in range(0,P+1):
            for x in range(0,min(j,K)+1):
                dp[i][j] = max(dp[i][j], all_stacks[i-1][x]+dp[i-1][j-x])
    
    print('Case #{}: {}'.format(t, dp[N][P]))
