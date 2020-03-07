from collections import defaultdict

def seek_key(dct, value):
    for k,v in dct.items():
        if v == value: return k

def seek_interval(intervals, pos):
    for k,v in intervals.items():
        if (pos >= k) and (pos <= v):
            return (k,v)
    return (-1,-1)

def add_east_west(tab_interval, seek_pos, west=True):
    #find interval, where current position is
    (start_interval, end_interval) = seek_interval(tab_interval, seek_pos)
    #print('we have intervals: ', tab_interval)
    #print ('we are now in ({}, {})'.format(start_interval, end_interval))
    new_pos = 0
    if west == False:
        if end_interval+2 in tab_interval.keys():
            tab_interval[start_interval] = tab_interval[end_interval+2]
            new_pos = end_interval+1
            del tab_interval[end_interval+2]
        else: 
            tab_interval[start_interval] += 1
            new_pos = tab_interval[start_interval]
    else:
        if start_interval-2 in tab_interval.values():
            key = seek_key(tab_interval,start_interval-2)
            tab_interval[key] = end_interval
            new_pos = start_interval-1
            del tab_interval[start_interval]
                #otherwise we extend found interval by 1
        else: 
            tab_interval[start_interval-1] = end_interval
            new_pos = start_interval-1
            del tab_interval[start_interval]
        
        
    return new_pos
            
def add_north_south(tab_interval, seek_pos, debug=False):
    #find interval, where current position is
    (start_interval, end_interval) = seek_interval(tab_interval, seek_pos)
    #if (debug): print('we are looking for position {} and found interval {},{}'.format(seek_pos,start_interval, end_interval), tab_interval)
    if start_interval > 0:
        return False
    else:
        tab_interval[seek_pos] = seek_pos
        last_pos = seek_pos
        up_found = False
        #check if there is interval above this one
        if seek_pos-1 in tab_interval.values():
            key = seek_key(tab_interval, seek_pos-1)
            tab_interval[key] = seek_pos
            last_pos = key
            del tab_interval[seek_pos]
            up_found = True
                #check if there is interval below this one
        if seek_pos+1 in tab_interval.keys():
            tab_interval[last_pos] = tab_interval[seek_pos+1]
            del tab_interval[seek_pos+1]
            #if up_found == False: del tab_interval[seek_pos]
        return True

T = int(input())

for t in range(T):
    N, R, C, Sr, Sc = map(int, input().split())
    instructions = list(input())
    
    #init intervals
    row_intervals = defaultdict(dict)
    col_intervals = defaultdict(dict)
    
    #init first intervals
    row_intervals[Sr][Sc] = Sc
    col_intervals[Sc][Sr] = Sr
    cnt = 1
    for inst in instructions:
        cnt += 1
        if inst in ('W','E'):
            
            Sc = add_east_west(row_intervals[Sr], Sc, (True if inst=='W' else False))
            #while True:
            ok = add_north_south(col_intervals[Sc], Sr, True if cnt == 10 else False)
                #if ok == True: break
         
        elif inst in ('N','S'):

            Sr = add_east_west(col_intervals[Sc], Sr, (True if inst=='N' else False))
            #while True:
            ok = add_north_south(row_intervals[Sr], Sc, True if cnt == 11 else False)
                #if ok == True: break
        
        #print('We moved to position {},{}:'.format(Sr,Sc))
        #print ('we have row intervals: ', row_intervals)
        #print ('we have col intervals: ', col_intervals)
        
    print('Case #{}: {} {}'.format(t+1,Sr,Sc))
