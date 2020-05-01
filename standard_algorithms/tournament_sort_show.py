#caution, this is not how implementation of this algorithm should be done
#it is more to present, how this method works in general

from collections import defaultdict

show = True

def tournament_sort(input_data, no_of_buckets):
    #we split input data across available buckets
    #this way we simulate that we have portions of data kept separately
    buckets = defaultdict(list)
    
    bucket_no = 0
    for elem in input_data:
        buckets[bucket_no].append(elem)
        bucket_no += 1
        bucket_no %= no_of_buckets
    
    if show: 
        print('------------- Start ------------------')
        print('Buckets:')
    
    #actual sorting is as follows, each bucket is sorted separately
    #which can (actually should) happen in parallel
    for k,b in buckets.items():
        b.sort()
        if show: print(k, '->', b)
    if show: print('')
    #now, each bucket returns first item to middle layer where elements are then compared against each other
    #smallest one lands in target and is removed from bucket, it was taken from
    #then another element is taken from this bucket
    #continue until all buckets and middle layer are empty
    
    result = list()
    
    #initiate middle table which will keep partial results
    #take first element from each, already sorted, bucket
    #together with element, store number of bucket, where it was taken from 
    middle = list()
    for k,b in buckets.items():
        middle.append((b[0],k))            
    
    iter_no = 1
    while len(middle) > 0:
        
        if show: print ('-- Iteration {} --'.format(iter_no))
        iter_no += 1
        
        #sort middle table, we want to sort values only, hence we take first element from tuples that are present in this table
        middle.sort(key=lambda x: x[0])
        if show: print('middle ->', [x[0] for x in middle])
    
        #take out first value, together with its bucket number
        (bucket_value, bucket_no) = middle.pop(0)
        #remove this element from its source bucket
        buckets[bucket_no].pop(0)
        #and put to middle table new smallest number from the same bucket, as long as this bucket has some values left
        if len(buckets[bucket_no]) > 0: middle.append((buckets[bucket_no][0], bucket_no))
        #finally, add value of element taken from middle table to a final result
        result.append(bucket_value)
        if show:
            print('element taken -> ', bucket_value, '(from bucket {} )'.format(bucket_no))
            print('partial result ->', result)
            print('Buckets:')
            for k,b in buckets.items():
                print(k, '->', b)
            print('')
    
    #show result
    if show: print('Final result:', result)    
    return result
    
#example run
tournament_sort([1,4,2,5,3,6,7],3)
    
