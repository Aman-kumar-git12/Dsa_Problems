# Question : K Closest Points to Origin
# link : https://leetcode.com/problems/k-closest-points-to-origin/description/

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    newpoints = []
    for i in range(len(points)):
        dist = (points[i][0]**2 + points[i][1]**2)**0.5
        newpoints.append((dist , points[i][0] , points[i][1]))
    
    maxheap =[]
    for i in range(len(newpoints)):
        heapq.heappush(maxheap , (-newpoints[i][0] , newpoints[i][1] , newpoints[i][2]))
        if len(maxheap) > k :
            heapq.heappop(maxheap)
    ans = []
    
    while len(maxheap) > 0 :
        dist , first , sec = heapq.heappop(maxheap)
        ans.append([first , sec])
    return ans