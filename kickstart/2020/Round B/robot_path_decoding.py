T = int(input())

for t in range(1,T+1):
    
    path = input()
    
    col = row = 1
    mult = [1]
    m = 1
    for step in path:
        
        if step in ('123456789'):
            mult.append(int(step))
            m = m * mult[-1]
            continue
           
        elif step == 'S': 
            col += m
        elif step == 'N': 
            col -=m
        elif step == 'E': 
            row += m
        elif step == 'W': 
            row -=m
        
        elif step == ')':
            m = m // mult[-1]
            mult.pop()

    
    col = col % (10 ** 9)
    row = row % (10 ** 9)
    if col == 0: col = 10 ** 9
    if row == 0: row = 10 ** 9

    print("Case #{}: {} {}".format(t,row,col))
