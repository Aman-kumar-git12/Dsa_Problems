# Question : Shortest path in Directed Acyclic Graph
# link: https://www.geeksforgeeks.org/problems/shortest-path-in-directed-acyclic-graph/1




def shortestPath(self, V: int, E: int,edges: List[List[int]]) -> List[int]:
        

    adjlist = [[]for _ in range(V)]
    for s ,d , w in edges:
        adjlist[s].append((d , w))
        
        
    stack = []
    
    visited = [False] * V 
    topo_sort = [0]* V
    
    def dfs(node):
        visited[node] = True 
        
        for nei  ,wei in adjlist[node]:
            if not visited[nei]:
                dfs(nei)
        stack.append(node)
    
    dfs(0)
    
    
    distance = [float('inf')]* V
    distance[0] = 0 

    for node in stack[::-1] :
        dist = distance[node]
        for nei , wei in adjlist[node]:
            if dist + wei < distance[nei]:
                distance[nei] = dist + wei 
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            distance[i] = -1
    return distance