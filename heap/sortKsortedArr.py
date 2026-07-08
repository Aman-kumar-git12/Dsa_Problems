# Question : k sorted array
# link: https://www.geeksforgeeks.org/problems/k-sorted-array1610/1

def isKSortedArray(self, arr, n, k): 
    import heapq
    # #code here.
    maxheap = []
    sortedarr = []
    for i in range(len(arr)):
        heapq.heappush(maxheap , (arr[i] , i))
        if len(maxheap) > k + 1:
            poped , index = heapq.heappop(maxheap)
            sortedarr.append((poped , index))
        
    while len(maxheap) > 0:
        poped , index  = heapq.heappop(maxheap)
        sortedarr.append((poped , index))
    
    
    for i in range(len(sortedarr)):
        if abs(i - sortedarr[i][1]) > k:
            return "No"
    return 'Yes'
    