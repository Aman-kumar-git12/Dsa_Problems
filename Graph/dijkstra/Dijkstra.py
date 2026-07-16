# Question : Dijkstra Algorithm
# link : https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1


def dijkstra(self, V, edges, src):
    distance = [float('inf')] * V 
    
    import heapq 
    adjlist = [[] for _ in range(V)]
    for s , d , w in edges:
        adjlist[s].append((d , w))
        adjlist[d].append((s , w))
    
    heap = []
    heapq.heappush(heap , (0 , src))
    distance[src] = 0 
    
    
    while heap:
        dist , popnode = heapq.heappop(heap)
        # if longer path exist
        if dist > distance[popnode]:
            continue
        for nei , wei in adjlist[popnode]:
            if dist + wei < distance[nei]:
                distance[nei] = dist + wei
                heapq.heappush(heap , (distance[nei] , nei))
                
    return distance 
    