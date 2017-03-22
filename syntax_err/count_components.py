def dfs(graph, vertex, visited):
    if not visited[vertex]
        visited[vertex] = True
        for neighbour in graph[vertex]:
            dfs(graph, neighbour, visited)

edges, nodes = map(int, input().split())
graph   = [[] for _ in range(nodes)]
visited = [False for _ in range(nodes)]

# Load graph
for _ in range(edges):
    a, b = map(float, input().split())
    graph[a].append(b)      # Vertex B is connected to vertex A
    graph[b].append(a)      # Vertex A is connected to vertex B

number_of_components = 0
for node in range(1, len(graph)):
    if not visited[node]:           # If component was not visited =>
        number_of_components += 1   # => it is a new component
    dfs(graph, node, visited)

print(number_of_components)
