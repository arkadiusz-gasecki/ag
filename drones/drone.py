filename = 'busy_day.in'

import datetime
import math

f_obj = open(filename, 'r')

txt = f_obj.readlines()

##parse first line of the file
lst = txt[0].split()

ROWS = int(lst[0])
COLS = int(lst[1])
DRONES_NO = int(lst[2])
TURNS = int(lst[3])
PAYLOAD = int(lst[4])

print('ROWS = {}, COLS = {}, DRONES = {}, TURNS = {}, PAYLOAD = {}'.format(ROWS, COLS, DRONES_NO, TURNS, PAYLOAD))

## define needed classes
class Warehouse:
        def __init__(self,w_id,location,products):
                self.id = w_id
                self.location = location
                self.products = products
class Drone:
        def __init__(self, d_id, location, capacity):
                self.id = d_id
                self.location = location
                self.capacity = capacity

        def in_warehouse(self, coord):
                return coord in (list(map(lambda x: x.location, WAREHOUSES)))

        def calc_distance(self, src, tgt):
                ra = src[0]
                ca = src[1]
                rb = tgt[0]
                cb = tgt[1]
                return math.ceil(math.sqrt(math.pow(abs(ra - rb),2) + math.pow(abs(ca - cb),2)))

        def find_nearest_warehouse(self, skip_list):
                dst = -1
                w = -1
                warehouse_no = -1
                for w in WAREHOUSES:
                        warehouse_no = warehouse_no + 1
                        if w in skip_list:
                                continue
                        else:
                                calc_dst = calc_distance(self.location, w.location)
                                if (dst == -1) | (calc_dst < dst):
                                        dst = calc_dst
                                        w = warehouse_no
                if dst <> -1:
                        return w
                else:
                        return -1


class Order:
        def __init__(self, o_id, location, prods):
                self.id = o_id
                self.location = location
                self.prods = prods
                self.prod_weights = list()
                for p in prods:
                        self.prod_weights.append(PRODUCTS[p])
                self.total_weight = sum(self.prod_weights)

## gather information about products
NO_PRODUCTS = int(txt[1])
lst = txt[2].split()
PRODUCTS = list()
for elem in lst:
        PRODUCTS.append(int(elem))

#print(PRODUCTS)

## gather information about warehouses
NO_WAREHOUSES =  int(txt[3])
WAREHOUSES = list()
w_id = -1
for i in range(0,NO_WAREHOUSES):
        w_id = w_id + 1
        if i % 2 == 0:
                loc = list(map(int, txt[4+i].split()))
                prods = list(map(int, txt[5+i].split()))
                WAREHOUSES.append(Warehouse(w_id, loc, prods))

## define list of drones
DRONES = list()
for i in range(0,DRONES_NO):
        DRONES.append(Drone(i, WAREHOUSES[0].location, PAYLOAD))


print(WAREHOUSES[0])
##determine line number where orders start
order_line_start = 3 + 2 * NO_WAREHOUSES + 1
NO_ORDERS = int(txt[order_line_start])

order_list = txt[order_line_start+1:]
ORDERS = list()
order_index = 0

for i in range(0, len(order_list)):
        if i % 3 == 0:
                tgt = list(map(int,order_list[i].split()))
                items = int(order_list[i+1])
                prd = sorted(list(map(int,order_list[i+2].split())))
                weight = 0
                for itm in range(0,items):
                        weight = weight + PRODUCTS[prd[itm]]

                ORDERS.append(Order(order_index, tgt, prd))
                order_index = order_index + 1


#for o in ORDERS_SORTED:
#       print(o)


## let's code single order
so = ORDERS[30]
print(so)
