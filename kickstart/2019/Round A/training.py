#python3

import sys

#read test cases
T = int(input())
result = list()

for i in range(0,T):
    N,P = map(int,input().split())
    Ntab = list(map(int,input().split()))
    len_Ntab = len(Ntab)
    Ntab = sorted(Ntab, reverse=True)
    start_index = 0
    end_index = P-1
    min_training_time = -1
    Psum = sum(Ntab[0:P])
    while True:
        prev_element = 0 if start_index == 0 else Ntab[start_index-1]
        next_element = 0 if start_index == 0 else Ntab[end_index]
        Psum = Psum + next_element - prev_element
        training_time = P*Ntab[start_index] - Psum
        
        if (training_time < min_training_time) | (min_training_time == -1):
            min_training_time = training_time

        end_index += 1
        if end_index >= len_Ntab:
            break
        start_index += 1
    result.append(min_training_time)
        

for r in range(0,len(result)):
    print("Case #{}: {}".format(r+1, result[r]))
