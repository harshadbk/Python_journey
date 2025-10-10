def is_safe(vertex, graph, color, colors):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def solve_graph_coloring(vertex, graph, m, colors):
    if vertex == len(graph):
        return True

    # Try all colors
    for c in range(1, m + 1):
        if is_safe(vertex, graph, c, colors):
            colors[vertex] = c
            if solve_graph_coloring(vertex + 1, graph, m, colors):
                return True
            colors[vertex] = 0  # Backtrack

    return False

def graph_coloring(graph, m):
    n = len(graph)
    colors = [0] * n

    if solve_graph_coloring(0, graph, m, colors):
        print("Color assignment successful:")
        for v in range(n):
            print(f"Vertex {v} ---> Color {colors[v]}")
    else:
        print("No solution exists")

# Example graph (Adjacency list)
graph = [
    [1, 2],   # Vertex 0 connected to 1, 2
    [0, 2, 3],# Vertex 1 connected to 0, 2, 3
    [0, 1, 3],# Vertex 2 connected to 0, 1, 3
    [1, 2]    # Vertex 3 connected to 1, 2
]

# Number of colors
m = 3
graph_coloring(graph, m)
