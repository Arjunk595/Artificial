# its a example of Greedy Algorithms, 
# used in AI for efficient decision-making in graphs.

# Purpose of code:
    # to find MST from a graph. 
    # MST is essential in AI for applications like
        # 1 pathfinding,
        # 2 network design
        # 3 clustering algorithms
def prim(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True
    edges = []
    total_weight = 0

    for _ in range(n - 1):
        min_edge = (None, None, float('inf')) # min_edge is a tuple (u, v, weight)
        for u in range(n):
            if selected[u]:
                for v in range(n):
                    if not selected[v] and graph[u][v] and graph[u][v] < min_edge[2]:
                        min_edge = (u, v, graph[u][v])
        u, v, w = min_edge # unpacking the tuple
        edges.append((u,v,w))
        print(edges)
        total_weight += w
        selected[v] = True
    return edges, total_weight

# Example (adjacency matrix)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst, total_weight = prim(graph)
print(mst)
for u, v, w in mst:
    print(f"{u} -- {v} : {w}")
print(f"Total weight of MST: {total_weight}")