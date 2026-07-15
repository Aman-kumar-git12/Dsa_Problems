# Question : Directed Graph Cycle
# link : https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
def isCyclic(self, V, edges):
    # code here
    adjlist = [[]for i in range(V)]
    indegree = [0]*V
    for s , d in edges:
        indegree[d]+=1
        adjlist[s].append(d)
    
    
    # visited = [False]* V
    # previsited = [False ] * V
    
    # def dfs(node):
    #     visited[node] = True 
    #     previsited[node]  = True 
    #     for nei in adjlist[node]:
    #         if not visited[nei]:
    #             if dfs(nei):
    #                 return True 
    #         elif previsited[nei] :
    #             return True 
    #     previsited[node]  = False 
    
    # for i in range(V):
    #     if not visited[i]:
    #         if dfs(i):
    #             return True 
    # return False
    
    import heapq 
    heap = []
    for i in range(len(indegree)):
        if indegree[i]==0:
            heapq.heappush(heap , i)
    ans = []     
    while heap:
        popnode = heapq.heappop(heap)
        ans.append(popnode)
        for nei in adjlist[popnode]:
            indegree[nei]-=1
            if indegree[nei]==0:
                heapq.heappush(heap , nei)
    if len(ans) == V:
        return False 
    return True 