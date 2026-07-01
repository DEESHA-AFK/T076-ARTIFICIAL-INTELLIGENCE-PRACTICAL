from collections import deque

# Graph Representation
mumbai_map = {
    'Versova': ['Andheri', 'Juhu', 'Lokhandwala'],

    # Route 1
    'Andheri': ['Western Express Highway'],
    'Western Express Highway': ['Bandra'],

    # Route 2
    'Juhu': ['Santacruz'],
    'Santacruz': ['Bandra'],

    # Route 3
    'Lokhandwala': ['Oshiwara'],
    'Oshiwara': ['Andheri West'],
    'Andheri West': ['Bandra'],

    # Destination
    'Bandra': []
}

# Breadth First Search (BFS)
def bfs_shortest_path(graph, start, destination):

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == destination:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

# Driver Code
start_node = "Versova"
end_node = "Bandra"

path = bfs_shortest_path(mumbai_map, start_node, end_node)

print("Breadth First Search (BFS)")
print("--------------------------")
print("Source      :", start_node)
print("Destination :", end_node)
print("Shortest Path Found:")
print(" -> ".join(path))
print("Total Steps:", len(path) - 1)

# Graph Representation
mumbai_map = {
    'Versova': ['Andheri', 'Juhu', 'Lokhandwala'],

    # Route 1
    'Andheri': ['Western Express Highway'],
    'Western Express Highway': ['Bandra'],

    # Route 2
    'Juhu': ['Santacruz'],
    'Santacruz': ['Bandra'],

    # Route 3
    'Lokhandwala': ['Oshiwara'],
    'Oshiwara': ['Andheri West'],
    'Andheri West': ['Bandra'],

    # Destination
    'Bandra': []
}

# Iterative Depth First Search (DFS)
def iterative_dfs(graph, start, destination):

    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current == destination:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

# Driver Code
start_node = "Versova"
end_node = "Bandra"

path = iterative_dfs(mumbai_map, start_node, end_node)

print("Iterative Depth First Search (DFS)")
print("----------------------------------")
print("Source      :", start_node)
print("Destination :", end_node)
print("Path Found:")
print(" -> ".join(path))
print("Total Steps:", len(path) - 1)

from collections import deque
import time

# Graph Representation
mumbai_map = {
    'Versova': ['Andheri', 'Juhu', 'Lokhandwala'],

    # Route 1
    'Andheri': ['Western Express Highway'],
    'Western Express Highway': ['Bandra'],

    # Route 2
    'Juhu': ['Santacruz'],
    'Santacruz': ['Bandra'],

    # Route 3
    'Lokhandwala': ['Oshiwara'],
    'Oshiwara': ['Andheri West'],
    'Andheri West': ['Bandra'],

    # Destination
    'Bandra': []
}

# ---------------- BFS ----------------
def bfs(graph, start, destination):
    queue = deque([(start, [start])])
    visited = set([start])
    nodes = 0

    while queue:
        current, path = queue.popleft()
        nodes += 1

        if current == destination:
            return path, nodes

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, nodes


# ---------------- DFS ----------------
def dfs(graph, start, destination):
    stack = [(start, [start])]
    visited = set()
    nodes = 0

    while stack:
        current, path = stack.pop()
        nodes += 1

        if current == destination:
            return path, nodes

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None, nodes


# ---------------- Comparison ----------------
start = "Versova"
goal = "Bandra"

# BFS Performance
bfs_start = time.perf_counter()
bfs_path, bfs_nodes = bfs(mumbai_map, start, goal)
bfs_end = time.perf_counter()

# DFS Performance
dfs_start = time.perf_counter()
dfs_path, dfs_nodes = dfs(mumbai_map, start, goal)
dfs_end = time.perf_counter()

# Display Results
print("========== BFS ==========")
print("Path :", " -> ".join(bfs_path))
print("Steps:", len(bfs_path) - 1)
print("Nodes Visited:", bfs_nodes)
print("Execution Time:", bfs_end - bfs_start, "seconds")

print("\n========== DFS ==========")
print("Path :", " -> ".join(dfs_path))
print("Steps:", len(dfs_path) - 1)
print("Nodes Visited:", dfs_nodes)
print("Execution Time:", dfs_end - dfs_start, "seconds")

print("\n========== Comparison ==========")

if len(bfs_path) < len(dfs_path):
    print("BFS found the shorter path.")
elif len(bfs_path) > len(dfs_path):
    print("DFS found the shorter path.")
else:
    print("Both found paths of equal length.")

print("BFS Time :", bfs_end - bfs_start)
print("DFS Time :", dfs_end - dfs_start)



