def insert_sort(arr):
    
    for i in range(1,len(arr)):
        j = i
        while (j > 0) and (arr[j-1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

        
inp = [3,2,1,4,6,5,9,8,7]

insert_sort(inp)
print(inp)
        
