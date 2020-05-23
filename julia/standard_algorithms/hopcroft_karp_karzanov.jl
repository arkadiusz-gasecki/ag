#=
we need to define graph as a bipartite one
nodes are given in two sets, U and V
edges are given in one direction
second direction added afterwards automatically
code based on pseudocode from Wikipedia
=#

U = ['A','B','C','D','E']
V = ['F','G','H','I','J']
Edges = Dict(
	'A'=> Set(['F','G']),
	'B'=> Set(['F']),
	'C'=> Set(['G','H','I']),
	'D'=> Set(['I','J']),
	'E'=> Set(['I'])
	#other direction added in a loop afterwards
	#,'F'=> Set(['A','B']),
	#'G'=> Set(['A','C']),
	#'H'=> Set(['C']),
	#'I'=> Set(['C','D','E']),
	#'J'=> Set(['D'])
	)

for (src, tgt) in copy(Edges)
	for elem in tgt
		if (elem in Edges.keys) == true
			push!(Edges[elem], src)
		else
			Edges[elem] = Set(src)
		end
	end
end

queue = Vector{Char}()
pair_U = Dict()
pair_V = Dict()
distance = Dict()

function BFS()
	for u in U
		if pair_U[u] == '0'
			distance[u] = 0
			push!(queue,u)
		else
			distance[u] = 999999
		end
	end
	distance['0'] = 999999
	while length(queue) > 0
		u = pop!(queue)
		if distance[u] < distance['0']
			for v in Edges[u]
				if distance[pair_V[v]] == 999999
					distance[pair_V[v]] = distance[u] + 1
					push!(queue, pair_V[v])
				end
			end
		end
	end
	return distance['0'] != 999999
end

function DFS(u)
	if u != '0'
		for v in Edges[u]
			if distance[pair_V[v]] == distance[u] + 1
				if DFS(pair_V[v]) == true
					pair_V[v] = u
					pair_U[u] = v
					return true
				end
			end
		end
		distance[u] = 999999
		return false
	end
	return true
end




function Hopcroft_Karp()
	for u in U
		pair_U[u] = '0'
	end
	for v in V
		pair_V[v] = '0'
	end
	matching = 0
	while BFS() == true
		for u in U
			if pair_U[u] == '0'
				if DFS(u) == true
					matching += 1
				end
			end
		end
	end
	return matching
end

m = Hopcroft_Karp()

using Printf

@printf("Maximum cardinality matching is %d\n", m)
println("Selected edges are:")
for (k,v) in pair_U
	@printf("%s -> %s\n", k,v)
end
