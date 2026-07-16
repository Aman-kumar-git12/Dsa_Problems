# Question: Path with Maximum Probability
# link : https://leetcode.com/problems/path-with-maximum-probability/description/


def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    adjlist = [[]for _ in range(n)]
    for i in range(len(edges)):
        s = edges[i][0]
        d = edges[i][1]
        w = succProb[i]
        adjlist[s].append((d , w))
        adjlist[d].append((s , w))


    import heapq 
    probability = [float('-inf')] * n 

    heap = []
    heapq.heappush(heap , (-1 , start_node))
    probability[start_node] = 1


    while heap:
        dist , popnode = heapq.heappop(heap)
        prob = -dist
        if prob < probability[popnode]:
            continue
        for nei , wei in adjlist[popnode]:
            if prob * wei > probability[nei]:
                probability[nei] = prob * wei
                heapq.heappush(heap , (-probability[nei] , nei))
    
    if  probability[end_node] == float('-inf') :
        return 0  
    return probability[end_node]
        