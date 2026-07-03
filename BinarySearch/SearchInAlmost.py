# Question : Search in an Almost Sorted Array
# link  : https://www.geeksforgeeks.org/problems/search-in-an-almost-sorted-array/1

def findTarget(self, arr, target):
        
    start , end = 0 , len(arr)-1 
    n = len(arr)
    while start <= end:
        mid = end -  (end - start)//2 
        next = (mid + 1) % n
        prev = (mid + n -1) % n
        if arr[mid] == target:
            return mid
        elif arr[prev] == target:
            return prev 
        elif arr[next] == target:
            return next 
        elif arr[mid] < target:
            start = mid + 2 
        elif target < arr[mid]:
            end = mid -2 
    return -1 
    