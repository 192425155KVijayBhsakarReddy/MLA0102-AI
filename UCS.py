import heapq

def ucs(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    visited = {}

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited[node] = cost
        print(f"Visiting {node} with cost {cost}")

        if node == goal:
            print("Goal reached!")
            return cost

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, neighbor)
                )


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 3), ('C', 0)],
    'C': [('A', 4), ('F', 5), ('B', 0)],
    'D': [('B', 2)],
    'E': [('B', 3), ('F', 1)],
    'F': [('C', 5), ('E', 1)]
}

start_node = 'A'
goal_node = 'B'

ucs(graph, start_node, goal_node)
