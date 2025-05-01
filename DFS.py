visited = set()

def DFS(visited, graph, root):
    if root not in visited:
        print(root,end=" ")
        visited.add(root)
        for neighbour in graph[root]:
            DFS(visited, graph, neighbour)

if __name__=="__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    graph1={
        0:[1,2,3],
        1:[2],
        2:[4],
        3:[],
        4:[],
    }
    print("DFS IS: ")
    DFS(visited, graph1, 0)