#list of weights
w = [2,3,3,4,5]
#list of values
v = [3,4,3,5,8]

#knapsack capacity
W = 15

M = [ [ 0 for i in 1:W+1 ] for j in 1:length(w)+1]

#=
M[1][1] = 0
...
M[1][16] = 0
=#
#problematic, while indexing starts from 1

for i in 1:length(w)
    for j in 1:W+1
        if w[i] > j-1
            M[i+1][j] = M[i][j]
        else
            M[i+1][j] = max(M[i][j], M[i][j-w[i]] + v[i])
		end
	end
end

println("Answer is: ")
print(last(last(M)))