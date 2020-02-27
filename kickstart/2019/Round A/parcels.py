#python2.7

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
                        if (distance[r][c] > 0) and distance[r][c] > min_delivery_time:
                                min_delivery_time = distance[r][c]
        return min_delivery_time

T = int(input())
for t in range(T):
        grid = list()
        R,C = map(int,raw_input().split())
        for r in range(0,R):
                #read cols of row
                grid.append(raw_input())
        #print(grid)

        offices = list()
        empties = list()
        #determine coordinates of all delivery offices
        for r in range(0,R):
                for c in range(0,C):
                        if grid[r][c] == '1': offices.append((r,c))
                        else: empties.append((r,c))

        min_delivery_time = calc_min_delivery_time(offices, empties, R, C)
        for e in empties:
                temp_empties = empties[:]
                temp_empties.remove(e)

                temp_offices = offices[:]
                temp_offices.append(e)

                new_min = calc_min_delivery_time(temp_offices, temp_empties, R, C)
                #print(new_min)
                if new_min < min_delivery_time: min_delivery_time = new_min

        print("Case #{}: {}".format(t+1,min_delivery_time))
