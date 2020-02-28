from collections import defaultdict
from datetime import datetime
from copy import copy

def calc_freq(block):
    freqs = defaultdict(int)
	
    for i in range(len(block)):
        freqs[block[i]] += 1
	total_freqs[i] = copy(freqs)
	
def is_palindromic(block, L, R):
    odd_values = 0
    #R_freqs = total_freqs[R]
    #L_freqs = total_freqs[L-1]
    for char in block:
        odd_values += ( (total_freqs[R].get(char,0) - total_freqs[L-1].get(char,0)) % 2 )
        if odd_values > 1:
            return 0 
    return 1 

T = int(raw_input())
answers = {}

print(datetime.now())
for t in range(0,T):
    total_freqs = {}
    total_freqs[-1] = defaultdict(int)
    #N,Q = map(int,raw_input().split())
    N,Q = 10000,1
    #block = raw_input()
    f = open('input.txt','r')
    block = f.readline()
    f.close()
    #calc_freq(block)
    freqs = defaultdict(int)

    for i in range(len(block)):
        freqs[block[i]] += 1
        total_freqs[i] = dict(freqs)
    #print(total_freqs)
    answers[t] = 0
    for q in range(0,10000):
        #L,R = map( lambda k: int(k)-1,raw_input().split())
        L,R = 1,35
        #take substring
        #answers[t] += is_palindromic(list(set(block[L:R+1])),L,R)
        odd_values = 0
        bck = list(set(block[L:R+1]))
        for char in bck:
            odd_values += ( (total_freqs[R].get(char,0) - total_freqs[L-1].get(char,0)) % 2 )
            if odd_values > 1:
                break
        answers[t] += 1


print(datetime.now())
for i in range(len(answers)):
    print("Case #{}: {}".format(i+1,answers[i]))
