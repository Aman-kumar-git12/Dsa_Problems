# link : https://my.newtonschool.co/playground/code/qez70kswdbh3

def dfsOnGraph(n , edges):
    adjlist = [[] for _ in range(n)]
    for s,d in edges:
        adjlist[s].append(d)
        adjlist[d].append(s)
    
    visited = [False] * n 
    result = []
    
    def dfs(node):
        visited[node] = True 
        result.append(node)
        for nei in adjlist[node]:
            if not visited[nei]:
                dfs(nei)

    for node in range(n):
        if not visited[node]:
            dfs(node)

    return result 

        

        
