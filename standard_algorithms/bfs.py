
graph = {
        'U': ['A','B','C','D','E'],
        'A': ['F','G'],
        'B': ['F'],
        'C': ['G','H','I'],
        'D': ['I','J'],
        'E': ['I']
        }

visited = list()
queue = list()

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        n = queue.pop(0)
        print(n)
        
        if n in graph:
            for child in graph[n]:
                if child not in visited:
                    visited.append(child)
                    queue.append(child)
                    
bfs(visited, graph, 'U')
