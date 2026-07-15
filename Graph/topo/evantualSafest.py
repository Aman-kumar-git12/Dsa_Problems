# Question : Eventual Safest Nodes in a Directed Graph
# link : https://leetcode.com/problems/eventual-safe-states/description/


def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    import heapq 
    heap = []
    indegree = [0]*len(graph)

    adjlist = [[]for i in range(len(graph))]

    for src in range(len(graph)):
        for dest in graph[src]:
            indegree[src]+=1
            adjlist[dest].append(src)

    print(indegree)

    for i in range(len(indegree)):
        if indegree[i] == 0:
            heapq.heappush(heap ,i)

    ans = []

    while heap:
        popnode = heapq.heappop(heap)
        ans.append(popnode)
        for nei in adjlist[popnode]:
            indegree[nei]-=1
            if indegree[nei] == 0:
                heapq.heappush(heap ,nei)
                
    ans.sort()
    return ans