T = int(input())

for t in range(1,T+1):
    N = int(input())
    peaks = list(map(int,input().split()))
    
    num_peaks = 0
    i = 1
    while (i < N-1):
        prev_peak = peaks[i-1]
        next_peak = peaks[i+1]
        
        if (peaks[i] > prev_peak) and (peaks[i] > next_peak):
            num_peaks += 1
            i += 1
        
        i+=1
        
    print("Case #{}: {}".format(t,num_peaks))
