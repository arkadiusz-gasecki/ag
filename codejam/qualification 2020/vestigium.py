#python2.7
T = int(raw_input())
for t in range(1,T+1):
        N = int(raw_input())
        matrix = list()
        for n in range(N):
                row = map(int, raw_input().split())
                matrix.append(row)

        #calculate trace
        i=0
        trace = 0
        while i < N:
                trace += matrix[i][i]
                i += 1

        #check repeatability
        row_repeat = 0
        col_repeat = 0
        i = 0
        while i < N:
                repeat = dict()
                for elem in matrix[i]:
                        if elem in repeat.keys():
                                row_repeat += 1
                                break
                        else: repeat[elem] = 1

                repeat = dict()
                col = [ row[i] for row in matrix]
                for elem in col:
                        if elem in repeat.keys():
                                col_repeat += 1
                                break
                        else: repeat[elem] = 1
                i += 1

        print("Case #{}: {} {} {}".format(t, trace, row_repeat, col_repeat))
