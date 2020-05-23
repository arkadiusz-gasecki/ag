graph = Dict(
        'U'=> ['A','B','C','D','E'],
        'A'=> ['F','G'],
        'B'=> ['F'],
        'C'=> ['G','H','I'],
        'D'=> ['I','J'],
        'E'=> ['I']
        )

visited = Vector{Char}()
queue = Vector{Char}()

function bfs(visited, graph, node)
    push!(visited,node)
    push!(queue,node)
    
    while length(queue) > 0
        n = pop!(queue)
        println(n)
        
        if n in graph.keys
            for child in graph[n]
                if (child in visited) == false
                    push!(visited,child)
                    push!(queue,child)
				end
			end
		end
	end
end

bfs(visited, graph, 'U')
