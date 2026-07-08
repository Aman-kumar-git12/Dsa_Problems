# Question : Top K Frequent Elements
# link : https://leetcode.com/problems/top-k-frequent-elements/description/

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    map = {}
    for i in range(len(nums)):
        if nums[i] not in map:
            map[nums[i]] = 1 
        else :
            map[nums[i]] += 1
    newmap = []
    for i , j in map.items() :
        newmap.append((j , i))
    
    minheap  = []
    res = []
    for i in range(len(newmap)):
        heapq.heappush(minheap , newmap[i])
        if len(minheap) > k:
            heapq.heappop(minheap)

    while len(minheap) > 0:
        fre , ele = heapq.heappop(minheap)
        res.append(ele)
    return res