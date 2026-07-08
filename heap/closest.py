# Question : Find K Closest Elements
# link: https://leetcode.com/problems/find-k-closest-elements/description/

def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    # # time : O(nlogn)
    # # space : O(n)
    # if x > arr[-1]:
    #     return arr[-k:]
    # elif x < arr[0]:
    #     return arr[:k]
    # else:

    #     indarr = []
    #     for i in range(len(arr)):
    #         indarr.append((arr[i] , abs(arr[i] - x)))

    #     indarr.sort(key =lambda x : x[1])
    #     newarr = []
    #     for i in range(k):
    #         newarr.append(indarr[i][0])
    #     newarr.sort()
    #     return newarr

    # time O(nlogk)
    # space O(n) using heap
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