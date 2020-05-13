
filename = 'busy_day.in'

import drone_classes as dc



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


## gather information about products
NO_PRODUCTS = int(txt[1])
lst = txt[2].split()

for elem in lst:
    dc.PRODUCTS.append(int(elem))

#print(PRODUCTS)

## gather information about warehouses
NO_WAREHOUSES =  int(txt[3])
print('Number of warehouses is {}'.format(NO_WAREHOUSES))
w_id = -1
for i in range(0,2*NO_WAREHOUSES):
    
    if i % 2 == 0:
        w_id = w_id + 1
        loc = list(map(int, txt[4+i].split()))
        prods = list(map(int, txt[5+i].split()))
        print(w_id,loc, prods)
        dc.WAREHOUSES.append(dc.Warehouse(w_id, loc, prods))

## define list of drones

for i in range(0,DRONES_NO):
    dc.DRONES.append(dc.Drone(i, dc.WAREHOUSES[0].location, 0, PAYLOAD))


print(dc.WAREHOUSES)
##determine line number where orders start
order_line_start = 3 + 2 * NO_WAREHOUSES + 1
NO_ORDERS = int(txt[order_line_start])

order_list = txt[order_line_start+1:]

order_index = 0

for i in range(0, len(order_list)):
    if i % 3 == 0:
        tgt = list(map(int,order_list[i].split()))
        items = int(order_list[i+1])
        prd = sorted(list(map(int,order_list[i+2].split())))
        weight = 0
        for itm in range(0,items):
            weight = weight + dc.PRODUCTS[prd[itm]]

        dc.ORDERS.append(dc.Order(order_index, tgt, prd))
        order_index = order_index + 1


#for o in ORDERS_SORTED:
#       print(o)


## let's code single order
for so in dc.ORDERS:
    so.show_order()

for tick in range(0, TURNS):
    dc.sim_table[tick] = {}
    for drone in dc.DRONES:
        drone.current_tick = tick
        if drone.is_busy(tick): continue
    
        if drone.order == None and len(dc.ORDERS) > 0:
            drone.pick_next_order()
            tgt_wh = drone.seek_warehouse()
            if tgt_wh >= 0:
                drone.fly_to_location(dc.WAREHOUSES[tgt_wh].location, tick)
            else:
                drone.fly_to_location(drone.order.location, tick)
        
        if drone.in_warehouse(drone.tgt_wh_id):
            drone.pick_product()
            if len(drone.has_capacity_list()) > 0:
                tgt_wh = drone.seek_warehouse()
                if tgt_wh >= 0: drone.fly_to_location(dc.WAREHOUSES[tgt_wh].location, tick)
                else: drone.fly_to_location(drone.order.location, tick)
            else: drone.fly_to_location(drone.order.location, tick)
        
        if drone.in_order_location():
            drone.deliver_products()
            if len(drone.order.prods) == 0:
                drone.order = None
            else:
                tgt_wh = drone.seek_warehouse()
                drone.fly_to_location(dc.WAREHOUSES[tgt_wh].location, tick)

dc.log.close()
#print(dc.sim_table)

sim = open('simulation.txt','w')
for tick, value in dc.sim_table.items():
    text = str(tick) + '\t'
    for drone in dc.DRONES:
        if drone.id in value.keys():
            text += value[drone.id] + '\t'
        else:
            text += '\t'
    sim.write(text +'\n')
sim.close()
