''' 
we need to define graph as a bipartite one
nodes are given in two sets, U and V
edges are given in one direction
second direction added afterwards automatically
code based on pseudocode from Wikipedia
'''

U = ['A','B','C','D','E']
V = ['F','G','H','I','J']
Edges = {
	'A': {'F','G'},
	'B': {'F'},
	'C': {'G','H','I'},
	'D': {'I','J'},
	'E': {'I'}
	#other direction added in a loop afterwards
	#,'F': {'A','B'},
	#'G': {'A','C'},
	#'H': {'C'},
	#'I': {'C','D','E'},
	#'J': {'D'}
	}

for src, tgt in Edges.items():
	for elem in tgt:
		(Edges[elem].add(src)) if (elem in Edges) else (Edges.update({elem : {src}}))

queue = list()
pair_U = dict()
pair_V = dict()
distance = dict()

def BFS():
	for u in U:
		if pair_U[u] == 'NIL':
			distance[u] = 0
			queue.append(u)
		else:
			distance[u] = 999999
	distance['NIL'] = 999999
	while queue:
		u = queue.pop()
		if distance[u] < distance['NIL']:
			for v in Edges[u]:
				if distance[pair_V[v]] == 999999:
					distance[pair_V[v]] = distance[u] + 1
					queue.append(pair_V[v])
	return distance['NIL'] != 999999

def DFS(u):
	if u != 'NIL':
		for v in Edges[u]:
			if distance[pair_V[v]] == distance[u] + 1:
				if DFS(pair_V[v]) == True:
					pair_V[v] = u
					pair_U[u] = v
					return True
		distance[u] = 999999
		return False
	return True




def Hopcroft_Karp():
	for u in U:
		pair_U[u] = 'NIL'
	for v in V:
		pair_V[v] = 'NIL'
	matching = 0
	while BFS():
		for u in U:
			if pair_U[u] == 'NIL':
				if DFS(u) == True:
					matching += 1
	return matching

m = Hopcroft_Karp()
print('Maximum cardinality matching is %d' % m)
print('Selected edges are:')
for k,v in pair_U.items():
	print('%s -> %s' % (k,v))
