
import math

PRODUCTS = list()
WAREHOUSES = list()
DRONES = list()
ORDERS = list()

log = open('result.txt','w')
sim_table = dict()

## define needed classes
class Warehouse:
    def __init__(self,w_id,location,products):
        self.id = w_id
        self.location = location
        self.products = products
    
    def show_wh(self):
        print('Warehouse {} located at {} with products {}'.format(self.id, self.location, self.products))
                
    def has_product(self, p_id):
        return self.products[p_id] > 0
    
    def reduce_supply(self, p_id):
        self.products[p_id] -= 1
        
class Drone:
    def __init__(self, d_id, location, capacity, max_capacity):
        self.id = d_id
        self.location = location
        self.current_capacity = capacity
        self.max_capacity = max_capacity
        self.products_picked_up = list()
        self.start_tick = 0
        self.end_tick = 0
        self.order = None
        self.tgt_wh_id = -1
        self.current_tick = 0
    
    def is_busy(self, tick):
        if self.current_tick == 0: return False
        return ((tick >= self.start_tick) and (tick <= self.end_tick))
    
    def calc_distance(self, src, tgt):
        ra = src[0]
        ca = src[1]
        rb = tgt[0]
        cb = tgt[1]
        return math.ceil(math.sqrt(math.pow(abs(ra - rb),2) + math.pow(abs(ca - cb),2)))

    def in_warehouse(self, wh_id):
        if wh_id == -1: return False
        return (self.current_tick >= self.end_tick) and (self.location == WAREHOUSES[wh_id].location)
        
    def in_order_location(self):
        if self.order == None: return False
        return (self.current_tick >= self.end_tick) and (self.location == self.order.location)
    
    def pick_next_order(self):  
        self.order = ORDERS.pop(0)
        print('Tick {}: Drone {} took order:'.format(self.current_tick, self.id))
        self.order.show_order()
        sim_table[self.current_tick][self.id] = 'Order taken {}'.format(self.order.show_order())
        
    def has_capacity_list(self):
        allowed = list()
        for p in self.order.prods:
            if PRODUCTS[p] + self.current_capacity <= self.max_capacity:         
                allowed.append(p)
        return allowed
    
    def seek_warehouse(self):
        products_from_order = self.has_capacity_list()
        if len(products_from_order) == 0: return -1
        #take product that can be still taken
        min_dst = 999999999
        tgt_wh_id = -1
        for p in products_from_order:
            for wh_id, warehouse in enumerate(WAREHOUSES):
                if warehouse.has_product(p):
                    dst = self.calc_distance(self.location, warehouse.location)
                    if dst < min_dst:
                        min_dst = dst
                        tgt_wh_id = wh_id
        self.tgt_wh_id = tgt_wh_id
        #print('Tick {}: Drone {} found warehouse {} with product {}'.format(self.current_tick, self.id, self.tgt_wh_id, self.products_to_pick_up))
        #sim_table[self.current_tick] = {self.id: 'Products to pick up {}'.format(self.products_to_pick_up)}
        return tgt_wh_id
    
    def fly_to_location(self, tgt, s_tick):
        dst = self.calc_distance(self.location, tgt)
        self.start_tick = s_tick
        self.end_tick = s_tick + dst
        print('Drone {} start flying from {} to {} at {} till {}'.format(self.id, self.location, tgt, self.start_tick, self.end_tick))
        self.location = tgt
        
    def pick_product(self):
        
        for p in self.order.prods:
            if WAREHOUSES[self.tgt_wh_id].has_product(p) and (self.current_capacity + PRODUCTS[p] <= self.max_capacity) :
                print('Tick {}: Drone {} is taking product {}'.format(self.current_tick,self.id, p))
                
                self.order.prods.remove(p)

                self.products_picked_up.append(p)
                self.current_capacity += PRODUCTS[p]
                WAREHOUSES[self.tgt_wh_id].reduce_supply(p)
                print('Drone capacity is now {}'.format(self.current_capacity))
                print('Products taken are {}'.format(self.products_picked_up))
                
                log.write(str(self.id) + ' L ' + str(self.tgt_wh_id) + ' ' + str(p) +  ' 1\n')
            
        if self.id in sim_table[self.current_tick]:
            sim_table[self.current_tick][self.id] += ';' + 'Products taken: {}'.format(self.products_picked_up)
        else:
            sim_table[self.current_tick][self.id] =  'Products taken: {}'.format(self.products_picked_up)

    def deliver_products(self):
        log.write(str(self.id) + ' D ' + str(self.order.id) + ' ' + str(self.products_picked_up[-1]) + ' 1\n')
        sim_table[self.current_tick] = {self.id: 'Products delivered: {}'.format(self.products_picked_up) }
        print('Tick {}: Drone {} delivered products {}'.format(self.current_tick, self.id, self.products_picked_up))
        while self.products_picked_up:
            p = self.products_picked_up.pop()
            self.current_capacity -= PRODUCTS[p]
        print('Drone {} capacity reduced to {}'.format(self.id, self.current_capacity) )
        if len(self.order.prods) == 0:
            print('Tick {}: Drone {} completed order {}'.format(self.current_tick, self.id, self.order.id))
            sim_table[self.current_tick][self.id] += 'completed order {}'.format(self.order.id)
            sim_table[self.current_tick][self.id] += ';products picked up: {}'.format(self.products_picked_up)

class Order:
    def __init__(self, o_id, location, prods):
        self.id = o_id
        self.location = location
        self.prods = prods
        self.prod_weights = list()
        for p in prods:
            self.prod_weights.append(PRODUCTS[p])
        self.total_weight = sum(self.prod_weights)
        
    def show_order(self):
        return('Order {}, located at {}, with products {}'.format(self.id, self.location, self.prods))
