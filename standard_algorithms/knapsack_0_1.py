
#list of weights
w = [0,2,3,3,4,5]
#list of values
v = [0,3,4,3,5,8]

#knapsack capacity
W = 15

M = [ [ 0 for i in range(0,W+1) ] for j in range(0,len(w))]



for i in range(1,len(w)):
    for j in range(1,W+1):
        if w[i] > j:
            M[i][j] = M[i-1][j]
        else:
            M[i][j] = max(M[i-1][j], M[i-1][j-w[i]] + v[i])

print("Answer is: ")            
print(M[-1][-1])
