#only test set 1
from collections import defaultdict

def set_distance(grid,w,k,R,C,dst,visited):
    global init_K
    if (w >= 0) and (k >= 0) and (w < R) and (k < C):
        if (grid[w][k] == None) or (dst < grid[w][k]):
            grid[w][k] = dst
            visited.append((w,k)) 
            

def bfs(R, C, grid, offices):
    temp_grid = [[0 for i in range(0,C)] for j in range(0,R)]
    #mark empties
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '1': temp_grid[r][c] = 0
            else: temp_grid[r][c] = None 
    
    visited = offices.copy()
    
    while len(visited) > 0:
        elem = visited.pop()
        w,k = elem[0],elem[1]
        dst = temp_grid[w][k] + 1
        set_distance(temp_grid,w-1,k,R,C,dst,visited)
        set_distance(temp_grid,w+1,k,R,C,dst,visited)
        set_distance(temp_grid,w,k-1,R,C,dst,visited)
        set_distance(temp_grid,w,k+1,R,C,dst,visited)
    return temp_grid
    
T = int(input())
for t in range(T):
    grid = list()
    R,C = map(int,input().split())
    for r in range(R):
        #read cols of row
        grid.append(input())

    offices = list()
    empties = list()
    #determine coordinates of all delivery offices
    for r in range(0,R):
        for c in range(0,C):
            if grid[r][c] == '1': offices.append((r,c))
            else: empties.append((r,c))
    
    g = bfs(R,C, grid, offices)
    K = 0
    for (r,c) in empties:
        K = max(K, g[r][c])

    minSumK = defaultdict(lambda: 9999999)
    maxSumK = defaultdict(lambda: -9999999)
    minDifK = defaultdict(lambda: 9999999)
    maxDifK = defaultdict(lambda: -9999999)

    for (r,c) in empties:
        for k in range(K):
            if g[r][c] > k:
                minSumK[k] = min(r+c, minSumK[k])
                maxSumK[k] = max(r+c, maxSumK[k])
                minDifK[k] = min(r-c, minDifK[k])
                maxDifK[k] = max(r-c, maxDifK[k])
    
    minMax = dict()
    for k in range(K):
        rangeSum = maxSumK[k] - minSumK[k]
        rangeDif = maxDifK[k] - minDifK[k]
        s = min(rangeSum , rangeDif)
        b = max(rangeSum , rangeDif)
        
        minMax[k] = b // 2
        if (b % 2 == 1): minMax[k] += 1
        if (b % 2 == 0) and (b == s) and (((minSumK[k] + minDifK[k]) % 2) == 1):  minMax[k] += 1

    if (K == 0):
        print("Case #{}: {}".format(t+1,K))
    else:
        k_found = False
        for k,v in minMax.items():
            if k >= v:
                print("Case #{}: {}".format(t+1,k))
                k_found = True
                break
        if (k_found == False): print("Case #{}: {}".format(t+1,K))
