T = int(input())

for t in range(1,T+1):
    N,B = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    solution = 0
    total_price = 0
    for elem in A:
        if total_price+elem <= B:
            solution += 1
            total_price += elem
        else: break
    
    print('Case #{}: {}'.format(t, solution))
