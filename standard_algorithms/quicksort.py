data = [9,5,7,4,2,8,1,10,6,3]

def quicksort(input_data, left, right):
    if left < right:
        i = DivideInputData(input_data, left, right)
        quicksort(input_data, left, i-1)
        quicksort(input_data, i+1, right)
        
def DivideInputData(input_data, left, right):
    #divide_index = SelectDivideIndex(left, right)
    pivot = input_data[right]
    #Switch(input_data, divide_index, right)
    
    current_position = left
    for i in range(left, right):
        if input_data[i] < pivot:
            input_data[current_position], input_data[i] = input_data[i], input_data[current_position]
            current_position += 1
            
    input_data[current_position], input_data[right] = input_data[right], input_data[current_position]
    return current_position

    

quicksort(data,0,len(data)-1)
print(data)
