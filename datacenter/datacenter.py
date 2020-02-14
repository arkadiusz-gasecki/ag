filename = 'dc.in'

import datetime

with open(filename) as f_obj:
        line_no = 1
        for line in f_obj:
                lst = line.split()

                if line_no == 1:
                        R = int(lst[0])
                        S = int(lst[1])
                        U = int(lst[2])
                        P = int(lst[3])
                        M = int(lst[4])
                        print("R = {}, S = {}, U = {}, P = {}, M = {}".format(R,S,U,P,M))
                        break
                else:
                        break


#prepare matrix that will be populated with servers
DC = [ [0 for i in range(0,S)] for j in range(0,R) ]
DC2 = [ [0 for i in range(0,S)] for j in range(0,R) ]

with open(filename) as f_obj:
        #second iteration to determine unavailable slots
        broken_slots = list()
        line_no = 1
        for line in f_obj:
                lst = line.split()
                if ((line_no > 1) & (line_no <= (U+1))):
                        broken_slots.append((int(lst[0]), int(lst[1])))
                        DC[int(lst[0])][int(lst[1])] = -1
                elif line_no >= (U+1):
                        break
                line_no = line_no + 1

#define list of servers
with open(filename) as f_obj:
        servers = list()
        line_no = 1
        for line in f_obj:
                lst = line.split()
                if line_no > (U+1):
                        servers.append((int(lst[0]), int(lst[1])))
                line_no = line_no + 1


#define all 45 pools
pools = [ list() for i in range(0,P)]
servers = sorted(servers, key=lambda x: x[1], reverse=True)

#organize pools by assigning each server from servers list to each pool iteratively

pool_no = 0
for s in servers:
        pools[pool_no].append(s)
        pool_no = (pool_no + 1) % P


for i in range(0,len(pools)):
        sum = 0
        for p in pools[i]:
                sum = sum + p[1]
        print('Size of pool {} is {}'.format(i, sum))


ass_row = 0
ass_col = 0
#for each pool, we take a server and assign it sequentially to rows
for i in range(0,P):
        pool = pools[i]
        #take a server from pool
        for srv in pool:
                ssize = srv[0]
                capa = srv[1]
                bool_fits = True

                while True:
                        if ass_row >= R:
                                break

                        bool_fits = True

                        for c in range(0, ssize):
                                if (ass_col + c) >= S:
                                        bool_fits = False
                                        ass_row = ass_row + 1
                                elif DC2[ass_row][ass_col+c] <> 0:
                                        bool_fits = False

                        if bool_fits == True:
                                for c in range(0, ssize):
                                        DC2[ass_row][ass_col+c] = capa + (i+1)*1000
                                break
                        else:
                                ass_col = ass_col + ssize

        ass_row = (ass_row + 1) % R
        ass_col = 0


def find_place(row_no, ssize, capa, pool_index):
        ass_col = 0
        while True:
                bool_fits = True
                leave_loop = False
                if (ass_col + ssize) >= S:
                        bool_fits = False
                        leave_loop = True
                else:
                        for c in range(0, ssize):
                                if DC[row_no][ass_col+c] <> 0:
                                        bool_fits = False
                                        ass_col = ass_col + ssize
                                        break

                if bool_fits == True:
                        for c in range(0, ssize):
                                DC[row_no][ass_col+c] = capa + (pool_index+1)*1000
                        leave_loop = True

                if leave_loop == True:
                        break
        return bool_fits


pool_index = 0
row_no = 0
while True:

        if len(pools[pool_index]) > 0:
                srv = pools[pool_index].pop(0)
        ssize = srv[0]
        capa = srv[1]

        tmp_row_no = row_no
        while True:
                fit = find_place(tmp_row_no, ssize, capa, pool_index)
                if fit:
                        print('Found place for server from pool {}, size {}, capacity {} in row {}'.format(pool_index, ssize, capa, row_no))
                        break
                else:
                        tmp_row_no = (tmp_row_no + 1) % R
                if tmp_row_no == row_no:
                        break

        pool_index = pool_index + 1
        if pool_index >= P:
                pool_index = 0
                row_no = row_no + 1
        if row_no >= R:
                break

for i in range(0,R):
        print(DC2[i])

for i in range(0,len(pools)):
        print(pools[i])


capacity_dct = {}
## calculate capacity
def calc_capacity(row_to_exclude):

        row_no = -1
         col_no = -1
        for row in DC:
                row_no = row_no + 1
                col_no = -1
                if row_no == row_to_exclude :
                        continue
                for col in row:
                        col_no = col_no + 1
                        pool_no = col // 1000
                        capa = col % 1000
                        if (col_no+1 < S):
                                if (col == DC[row_no][col_no+1]):
                                        continue
                                else:
                                        if pool_no in capacity_dct:
                                                capacity_dct[pool_no] = capacity_dct[pool_no] + capa
                                        else:
                                                capacity_dct[pool_no] = capa
        #sum_capacity
        tot = 10000000
        for k,v in capacity_dct.items():
                if (k >= 1) & (k <= 45) & (v < tot):
                        tot = v
        #print(capacity_dct)
        print('Row excluded {}, total capacity: {}'.format(row_to_exclude, tot))


for i in range(0,R):
        calc_capacity(i)
