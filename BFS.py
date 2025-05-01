import collections
# BFS
def bfs(graph,root):
    visited=set()
    queue=collections.deque([root])
    while queue:
        vertex=queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex]:
                if i not in visited:
                    queue.append(i)
    print(visited)
# DFS
visited1 = set()

def DFS(visited1, graph, root):
    if root not in visited1:
        print(root,end=" ")
        visited1.add(root)
        for neighbour in graph[root]:
            DFS(visited1, graph, neighbour)
   
if __name__=="__main__":
    graph={0:[1,2,3],1:[0,2],2:[0,1,4],3:[0],4:[2]}
    
    graph1={
        0:[1,2,3],
        1:[2],
        2:[4],
        3:[],
        4:[],
    }
    
    bfs(graph,0)
    DFS(visited1,graph1,0)
    
#1. Time complexity for DFS & BFS
    # O(V + E) => V : number of vertices, E : number of edges

#2. Space complexity
    #DFS : O(v) for recursion stact in worst case
    #BFS : O(v) for queue and visited set

#3. DFS $ BFS are traversal algorithms.
