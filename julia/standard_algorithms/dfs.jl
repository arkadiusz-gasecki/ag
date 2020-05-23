graph = Dict(
        'U'=> ['A','B','C','D','E'],
        'A'=> ['F','G'],
        'B'=> ['F'],
        'C'=> ['G','H','I'],
        'D'=> ['I','J'],
        'E'=> ['I']
        )

visited = Vector{Char}()

function dfs(visited, graph, node)
    if (node in visited) == false
        println(node)
        push!(visited,node)
        if node in graph.keys
            for n in graph[node]
                dfs(visited, graph, n)
			end
		end
	end
end
                    
dfs(visited, graph, 'U')
