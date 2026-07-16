# Question : Network Delay Time
# link : https://leetcode.com/problems/network-delay-time/description/

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    adjlist = [[]for _ in range(n)]
    for s , d , w in times:
        adjlist[s-1].append((d-1 , w))


    import heapq 
    distance = [float('inf')] * n 
    heap = []
    heapq.heappush(heap , (0 , k-1))
    distance[k-1] = 0 


    while heap:
        dist , popnode = heapq.heappop(heap)
        for nei , wei in adjlist[popnode]:
            if dist + wei < distance[nei]:
                distance[nei] = dist + wei 
                heapq.heappush(heap , (distance[nei] , nei))

    for i in distance:
        if i == float('inf'):
            return -1
    return max(distance)