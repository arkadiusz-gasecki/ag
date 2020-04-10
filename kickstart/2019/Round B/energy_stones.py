import math

T = int(input())

for t in range(1,T+1):
    N = int(input())
    stones = list()
    total_time = 0
    for n in range(N):
        #seconds, energy, losing
        x = list(map(int, input().split()))

        stones.append(x)
        total_time += stones[-1][0]
    
    stones.sort(key=lambda x: math.inf if x[2] == 0 else x[0]/x[2], reverse=False)
    
    
    M = [[0 for j in range(0,total_time+1)] for i in range(0,len(stones)+1)]

    for time in reversed(range(0,total_time+1)):
        for i in reversed(range(0,len(stones))):
            
            energy_of_stone_by_time_i = max(0, stones[i][1] - time*stones[i][2])
        
            if time+stones[i][0] > total_time: future = 0
            else: future = M[i+1][time+stones[i][0]]

            M[i][time] = max(M[i+1][time] , energy_of_stone_by_time_i + future)

    print("Case #{}: {}".format(t,M[0][0]))
