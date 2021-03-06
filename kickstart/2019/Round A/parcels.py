from collections import defaultdict

def set_distance(grid,w,k,R,C,dst,visited):
    global init_K
    if (w >= 0) and (k >= 0) and (w < R) and (k < C):
        if (grid[w][k] == None):
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
        elem = visited.pop(0)
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
            offices.append((r,c)) if grid[r][c] == '1' else empties.append((r,c))
    
    g = bfs(R,C, grid, offices)
    K = 0
    for (r,c) in empties:
        K = max(K, g[r][c])
        
    L = 0
    R = K
    last_k = K
    
    while L < R:
        k = (L+R) // 2
    
        minSum = 9999999
        maxSum = -9999999
        minDiff = 9999999
        maxDiff = -9999999
        for (r,c) in empties:
            if g[r][c] > k:
                minSum = min(minSum, r+c)
                maxSum = max(maxSum, r+c)
                minDiff = min(minDiff, r-c)
                maxDiff = max(maxDiff, r-c)
                
        rangeSum = maxSum - minSum
        rangeDif = maxDiff - minDiff
        s = min(rangeSum , rangeDif)
        b = max(rangeSum , rangeDif)
        
        minMax = b // 2
        if (b % 2 == 1): minMax += 1
        if (b % 2 == 0) and (b == s) and (((minSum + minDiff) % 2) == 1):  minMax += 1
        
        if minMax <= k:
            R=k
            last_k = k
        else:
            L=k+1
  
    if (K == 0):
        print("Case #{}: {}".format(t+1,K))
    else:
        print("Case #{}: {}".format(t+1,last_k))
