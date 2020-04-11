def getMaxArea(hist):
    stack = list()
    max_area = 0
    
    i = 0
    n = len(hist)
    while (i < n):
        if (len(stack) == 0) or (hist[stack[0]] <= hist[i]):
            stack.insert(0,i)
            i += 1
            #print(stack)
        else:
            tp = stack.pop(0)
            ind = (i if len(stack) == 0 else i - stack[0] - 1)
            #print("Ind is {} - {} - 1 = {}".format(i, stack[0], ind))
            area_with_top = hist[tp] * ind
            #print("Top area is {}".format(area_with_top))
            max_area = max(max_area, area_with_top)
            #print(stack)
            
    while len(stack) > 0:
        tp = stack.pop(0)
        ind = (i if len(stack) == 0 else i - stack[0] - 1)
        area_with_top = hist[tp] * ind
        max_area = max(max_area, area_with_top)
        #print(stack)
    
    return max_area

histogram = [5,35,50,25,10]
print(getMaxArea(histogram))
