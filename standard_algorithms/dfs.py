
graph = {
        'U': ['A','B','C','D','E'],
        'A': ['F','G'],
        'B': ['F'],
        'C': ['G','H','I'],
        'D': ['I','J'],
        'E': ['I']
        }

visited = list()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        if node in graph:
            for n in graph[node]:
                dfs(visited, graph, n)
                    
dfs(visited, graph, 'U')
