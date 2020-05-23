#=
caution, this is not how implementation of this algorithm should be done
it is more to present, how this method works in general
=#

using Printf

show = true

function tournament_sort(input_data, no_of_buckets)
    #we split input data across available buckets
    #this way we simulate that we have portions of data kept separately
    buckets = Dict()
    bucket_no = 0
	
    for elem in input_data
		if (bucket_no in keys(buckets)) == false
			buckets[bucket_no] = [elem]
		else
			push!(buckets[bucket_no],elem)
		end
		
        bucket_no += 1
        bucket_no %= (no_of_buckets)
	end
    
    if show
        println("------------- Start ------------------")
        println("Buckets:")
	end
    
    #actual sorting is as follows, each bucket is sorted separately
    #which can (actually should) happen in parallel
    for (k,b) in buckets
        buckets[k] = sort(b)
        if show
			println(k, "->", b)
		end
	end
    if show println("") end
    #now, each bucket returns first item to middle layer where elements are then compared against each other
    #smallest one lands in target and is removed from bucket, it was taken from
    #then another element is taken from this bucket
    #continue until all buckets and middle layer are empty
    
    result = Vector{Int64}()
    
    #initiate middle table which will keep partial results
    #take first element from each, already sorted, bucket
    #together with element, store number of bucket, where it was taken from 
    middle = []
    for (k,b) in buckets
        push!(middle,(b[1],k))
	end
    iter_no = 1
    while length(middle) > 0
        
        if show @printf("-- Iteration %d --\n",iter_no) end
        iter_no += 1
        
        #sort middle table, we want to sort values only, hence we take first element from tuples that are present in this table
        middle = sort(middle)
        if show println("middle ->", [x[1] for x in middle]) end
    
        #take out first value, together with its bucket number
        (bucket_value, bucket_no) = popfirst!(middle)
        #remove this element from its source bucket
        popfirst!(buckets[bucket_no])
        #and put to middle table new smallest number from the same bucket, as long as this bucket has some values left
        if length(buckets[bucket_no]) > 0
			push!(middle,(buckets[bucket_no][1], bucket_no))
		end
        #finally, add value of element taken from middle table to a final result
        push!(result,bucket_value)
        if show
            @printf("element taken -> %d (from bucket %d )\n", bucket_value, bucket_no)
            println("partial result ->", result)
            print("Buckets:")
            for (k,b) in buckets
                println(k, "->", b)
			end
            println("")
		end
	end
    
    #show result
    if show println("Final result:", result) end
    return result
end
    
#example run
tournament_sort([1,4,2,5,3,6,7],3)