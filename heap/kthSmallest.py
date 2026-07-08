# Question : Kth Smallest Element
# link : https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1


def kthSmallest(self, arr, k):
    import heapq 

    # O(nlogn)
    arr.sort()
    return arr[k-1]
    

    # O(nlogk)
    maxheap = []
    n = len(arr)
    i = 0
    while i < n:
        maxheap.append(arr[i])
        maxheap.sort()
        if len(maxheap) > k:
            maxheap.pop()
        i+=1
    return maxheap[-1]
    
    
    # O(n)
    n = len(arr)
    i = 0
    heap = []
    while i < n:
        heapq.heappush(heap , -arr[i])
        if len(heap) > k:
            heapq.heappop(heap)
        i+=1
    return -heap[0]
    
    