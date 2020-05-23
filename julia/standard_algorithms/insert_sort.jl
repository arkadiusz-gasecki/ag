function insert_sort(arr)
    
    for i in 2:length(arr)
        j = i
        while j > 1 && arr[j-1] > arr[j]
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
		end
	end
end

inp = [3,2,1,4,6,5,9,8,7]

insert_sort(inp)
print(inp)