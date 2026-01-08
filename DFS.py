def dfs(graph, start, visited):
    visited.add(start)          
    print(start, end=" ") 

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# -------- INPUT --------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()
start_node = 'A'

dfs(graph, start_node, visited)
