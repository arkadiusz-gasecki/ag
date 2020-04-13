#only test set 1

def check_digits(n):
    for digit in str(n):
        if int(digit) % 2 == 1:
            return False
    return True

T = int(input())

for t in range(1,T+1):
    N = int(input())
    
    i=0
    while i <= N:
        if(check_digits(N+i)) or (check_digits(N-i)):
            break
        i += 1
    
    print("Case #{}: {}".format(t,i))
