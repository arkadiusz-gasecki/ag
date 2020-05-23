function dutch_flag(arr, mid_val)
    i = 1
    j = 1
	k = length(arr)
    while j <= k
        if arr[j] < mid_val
			arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elseif arr[j] > mid_val
			arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else
            j += 1
        end
    end
	return arr
end

inp = [0,1,2,2,2,1,0,0,1,1,2,0,1]

dutch_flag(inp,1)
print(inp)
