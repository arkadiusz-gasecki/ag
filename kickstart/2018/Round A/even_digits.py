
def make_smaller(lst):
    
    make_eight = False
    for i, digit in enumerate(lst):
        if make_eight: lst[i] = 8
        elif digit % 2 == 1:
            lst[i] -= 1
            make_eight = True
    
    smaller = int("".join(list(map(str,lst))))
    return smaller    

def make_bigger(lst):
    
    make_zero = False
    nine = False
    nine_index = 0
    for i, digit in enumerate(lst):
        if make_zero: lst[i] = 0
        elif digit % 2 == 1:
            make_zero = True
            if digit == 9:
                nine = True
                nine_index = i
                lst[i] = 0
            else:
                lst[i] += 1
            
        
    if nine:
        sublst = lst[0:nine_index]
        sublst.insert(0,0)
        
        for i in reversed(range(0,len(sublst))):
            if sublst[i] < 8 :
                sublst[i] += (1 + (sublst[i]%2+1)%2)
                break
            else:
                sublst[i] = 0
        newlist = sublst + lst[nine_index:]
        bigger = int("".join(list(map(str,newlist))))
        return bigger
    else:
        bigger = int("".join(list(map(str,lst))))
        return bigger
            
            

T = int(input())

for t in range(1,T+1):
    N = int(input())
    
    lst = list(map(int,list(str(N))))
    S = make_smaller(lst.copy())
    B = make_bigger(lst.copy())
    plus = B - N
    minus = N - S
    print("Case #{}: {}".format(t,min(plus,minus)))
    
