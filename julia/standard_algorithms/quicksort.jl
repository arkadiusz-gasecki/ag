data = [9,5,7,4,2,8,1,10,6,3]

function quicksort(input_data, left, right)
    if left < right
        i = DivideInputData(input_data, left, right)
        quicksort(input_data, left, i-1)
        quicksort(input_data, i+1, right)
	end
end

function DivideInputData(input_data, left, right)
    #divide_index = SelectDivideIndex(left, right)
    pivot = input_data[right]
    #Switch(input_data, divide_index, right)
    
    current_position = left
    for i in left:right
        if input_data[i] < pivot
            input_data[current_position], input_data[i] = input_data[i], input_data[current_position]
            current_position += 1
		end
	end
            
    input_data[current_position], input_data[right] = input_data[right], input_data[current_position]
    return current_position
end

    

quicksort(data,1,length(data))
print(data)