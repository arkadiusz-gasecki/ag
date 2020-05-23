using Printf

function getMaxArea(hist)
    stack = Vector{Int}()
    max_area = 0
    
    i = 1
    n = length(hist)
    while i <= n
        if (length(stack) == 0) || (hist[last(stack)] <= hist[i])
            push!(stack,i)
            i += 1
            #print(stack)
        else
            tp = pop!(stack)
            ind = (length(stack) == 0 ? i : i - last(stack))
            #@printf("Ind is %d - %d = %d", i, last(stack), ind)
            area_with_top = hist[tp] * (ind-1)
            #@printf("Top area is %d",area_with_top)
            max_area = max(max_area, area_with_top)
            #print(stack)
		end
	end
            
    while length(stack) > 0
        tp = pop!(stack)
        ind = (length(stack) == 0 ? i : i - stack[1])
        area_with_top = hist[tp] * (ind-1)
        max_area = max(max_area, area_with_top)
        #print(stack)
	end
    
    return max_area
end

histogram = [5,35,50,25,10]
print(getMaxArea(histogram))