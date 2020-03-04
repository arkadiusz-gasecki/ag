
def show_grid(grid):
    for line in grid:
        print(line)


def set_distance(grid,w,k,R,C,dst,visited):
    if (w >= 0) and (k >= 0) and (w < R) and (k < C):
        if (grid[w][k] == None) or (dst < grid[w][k]):
            grid[w][k] = dst
            visited.append((w,k)) 
            

def bfs(R, C, offices):
    temp_grid = [[0 for i in range(0,C)] for j in range(0,R)]
    #mark empties
    for r in range(R):
        for c in range(C):
            if (r,c) in offices: temp_grid[r][c] = 0
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

def calc_dst(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1 - c2)

def calc_min_delivery_time(offices, empties, R, C):
    distance = [[0 for i in range(0,C)] for j in range(0,R)]
    for e in empties:
        r,c = (e[0],e[1])
        distance[r][c] = R+C
        for o in offices:
            dst = calc_dst(r,c,o[0],o[1])
            if dst < distance[r][c]:
                distance[r][c] = dst
         #calculate miminum delivery time
    min_delivery_time = 0
    for r in range(0,R):
        for c in range(0,C):
            if (distance[r][c] > 0) and (distance[r][c] > min_delivery_time):
                min_delivery_time = distance[r][c]
    return min_delivery_time

def check_K(K,g,empties):
    to_check = list()
    possible_offices = list()
    for(r,c) in empties:
        if g[r][c] > K: to_check.append((r,c))
        possible_offices.append((r,c))
    #print('trying K={}'.format(K))
    #print('TO check we have ', to_check)
    #print('possible offices are' , possible_offices)
    is_ok = False
    for (r,c) in possible_offices:
        k_is_ok = True
        for (tgt_row,tgt_col) in to_check:
            if calc_dst(r,c,tgt_row,tgt_col) > K:
                k_is_ok = False
                break
        if k_is_ok == True:
            is_ok = True
            break
            
    return is_ok
    

T = int(input())
for t in range(T):
    grid = list()
    R,C = map(int,input().split())
    for r in range(0,R):
        #read cols of row
        grid.append(input())
        #print(grid)

    offices = list()
    empties = list()
    #determine coordinates of all delivery offices
    for r in range(0,R):
        for c in range(0,C):
            if grid[r][c] == '1': offices.append((r,c))
            else: empties.append((r,c))
    
    g = bfs(R,C, offices)
    #show_grid(g)
    #find maxium K after doing BFS
    K = 0
    for r in range(R):
        for c in range(C):
            if g[r][c] > K:K = g[r][c]
    
    #show_grid(g)
    #print('K is {}'.format(K))

    if K == 0:
        print("Case #{}: {}".format(t+1,K))
    else:
        L_bound = 0
        R_bound = K-1
        #while L_bound < R_bound:
        last_working_K = K
        while True:
            #print(L_bound, R_bound, K)
            #K = (R_bound+L_bound) // 2
            K = K-1
            
            to_check = list()
            minSum = 99999999
            maxSum = 0
            minDiff= 99999999
            maxDiff = 0
            for(r,c) in empties:
                if g[r][c] > K:
                    to_check.append((r,c))
                    minSum = min(minSum, r+c)
                    maxSum = max(maxSum, r+c)
                    minDiff = min(minDiff, r-c)
                    maxDiff = max(maxDiff, r-c)
            rangeSum = maxSum - minSum
            rangeDiff = maxDiff - minDiff
            s = min(rangeSum, rangeDiff)
            b = max(rangeSum, rangeDiff)
            
            minMax = b // 2
            if (b % 2 == 1): minMax += 1
            if (b % 2 == 0) and (b == s) and ((minSum+minDiff) % 2 == 1): minMax += 1
            
            #if minMax <= K:
            #    R_bound = K
            #else:
            #    L_bound = K+1
            if minMax <= K: last_working_K = K
            else: break
        
        #if check_K(K,g,empties) == False: K=K+1
        print("Case #{}: {}".format(t+1,int(last_working_K)))
    #min_delivery_time = calc_min_delivery_time(offices, empties, R, C)
    #for e in empties:
    #    temp_empties = empties[:]
    #    temp_empties.remove(e)

    #    temp_offices = offices[:]
    #    temp_offices.append(e)
        
    #    new_min = calc_min_delivery_time(temp_offices, temp_empties, R, C)
        #print(new_min)
    #    if new_min < min_delivery_time: min_delivery_time = new_min

    
