# Question : Find K Closest Elements
# link: https://leetcode.com/problems/find-k-closest-elements/description/

def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    import heapq
    maxheap = []
    indarr = []
    for i in range(len(arr)):
        indarr.append((abs(arr[i] - x) , arr[i]))

    # print(indarr)

    for i in range(len(indarr)):
        heapq.heappush(maxheap ,(-indarr[i][0], -indarr[i][1]))
        if len(maxheap) > k:
            heapq.heappop(maxheap)

    # print(maxheap)
    sortedarr = []
    while len(maxheap) > 0 :
        diff , ele = heapq.heappop(maxheap)
        sortedarr.append(-ele)
    sortedarr.sort()
    return sortedarr