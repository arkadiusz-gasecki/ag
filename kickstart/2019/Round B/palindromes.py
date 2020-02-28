from collections import defaultdict

def calc_freq(block):
    freqs = defaultdict(int)
    
    for i in range(len(block)):
        freqs[block[i]] += 1
        total_freqs[i] = dict(freqs)
    
def is_palindromic(L, R):
    odd_values = 0
    R_freqs = total_freqs[R]
    L_freqs = total_freqs[L-1]
    for char,r_cnt in R_freqs.items():
        odd_values += ( (r_cnt - L_freqs.get(char,0)) % 2 )
        if odd_values > 1:
            return 0 
    return 1 

T = int(input())
answers = {}

for t in range(0,T):
    total_freqs = {}
    total_freqs[-1] = defaultdict(int)
    N,Q = map(int,input().split())
    block = input()

    calc_freq(block)
    #print(total_freqs)
    #print(total_freqs)
    answers[t] = 0
    for q in range(0,Q):
        L,R = map( lambda k: int(k)-1,input().split())
        #take substring
        answers[t] += is_palindromic(L,R)

for i in range(len(answers)):
    print("Case #{}: {}".format(i+1,answers[i]))
