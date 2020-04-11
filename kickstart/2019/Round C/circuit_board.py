#only first test set

def getMaxArea(hist):
    stack = list()
    max_area = 0
    
    i = 0
    n = len(hist)
    while (i < n):
        if (len(stack) == 0) or (hist[stack[0]] <= hist[i]):
            stack.insert(0,i)
            i += 1
            #print(stack)
        else:
            tp = stack.pop(0)
            ind = (i if len(stack) == 0 else i - stack[0] - 1)
            #print("Ind is {} - {} - 1 = {}".format(i, stack[0], ind))
            area_with_top = hist[tp] * ind
            #print("Top area is {}".format(area_with_top))
            max_area = max(max_area, area_with_top)
            #print(stack)
            
    while len(stack) > 0:
        tp = stack.pop(0)
        ind = (i if len(stack) == 0 else i - stack[0] - 1)
        area_with_top = hist[tp] * ind
        max_area = max(max_area, area_with_top)
        #print(stack)
    
    return max_area


#----------------------------------------------------------------------------

T = int(input())

for t in range(1, T+1):
    R,C,K = map(int, input().split())
    board = list()
    for r in range(0,R):
        board.append(list(map(int, input().split())))
        
   # print(board)
    hist_board = [[1 for i in range(0, C)] for j in range(0,R)]
    
    for r in range(0,R):
        for c in range(1,C):
            if board[r][c] == board[r][c-1]:
                hist_board[r][c] = hist_board[r][c-1]+1
            else: hist_board[r][c] = 1
    
    #extract column from hist_board
    size = 0
    for c in range(0,C):
        col = [ hist_board[r][c] for r in range(0,R) ]
        size = max(size, getMaxArea(col))
    
    print("Case #{}: {}".format(t,size))
