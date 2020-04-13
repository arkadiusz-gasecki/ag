def dutch_flag(arr, mid_val):
    
    i = 0
    j = 0
    k = len(arr)
    while j < k:
        if arr[j] < mid_val:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > mid_val:
            k -= 1
            arr[j], arr[k] = arr[k], arr[j]
        else:
            j += 1
            
inp = [0,1,2,2,2,1,0,0,1,1,2,0,1]

dutch_flag(inp,1)
print(inp)
