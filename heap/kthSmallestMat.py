
# Question : Kth Smallest Element in a Sorted Matrix
# link : https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    maxheap = []
    for i in range(n):
        for j in range(n):
            heapq.heappush(maxheap , -matrix[i][j])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
    return -maxheap[0]
