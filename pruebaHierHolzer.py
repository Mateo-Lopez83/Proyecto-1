from collections import defaultdict

def find_eulerian_path(graph):
    def dfs(node):
        while graph[node]:
            neighbor = graph[node].pop()
            dfs(neighbor)
        path.append(node)
    
    # Count the degree of each vertex
    degree = defaultdict(int)
    for u, v in graph.items():
        degree[u] += len(v)
        for neighbor in v:
            degree[neighbor] += 1
    
    # Find the start node
    start_node = None
    for node, deg in degree.items():
        if deg % 2 == 1:
            if start_node is None:
                start_node = node
            else:
                return None  # No Eulerian path
    if start_node is None:
        start_node = next(iter(degree))
    
    # Hierholzer's algorithm
    path = []
    dfs(start_node)
    return path[::-1]

def build_graph(dominoes):
    graph = defaultdict(list)
    for u, v in dominoes:
        graph[u].append(v)
        graph[v].append(u)
    return graph

# Example
dominoes = [[1, 5], [2, 3], [3, 4], [4, 1], [1, 2], [5, 6], [6, 3]]
graph = build_graph(dominoes)
path = find_eulerian_path(graph)

# Check if the path is valid
if path:
    # Verify the path by checking if it covers all edges
    visited_edges = set()
    for i in range(len(path) - 1):
        visited_edges.add((path[i], path[i+1]))
        visited_edges.add((path[i+1], path[i]))
    if visited_edges == {(u, v) for u, neighbors in graph.items() for v in neighbors}:
        print("Eulerian Path:", path)
    else:
        print("The found path is not a valid Eulerian Path.")
else:
    print("No Eulerian Path exists for this set of dominoes.")
