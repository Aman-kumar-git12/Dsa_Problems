# Quesiton : Floor in a Sorted Array
# link : https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1


def findFloor(self, arr, x):
    start , end = 0 , len(arr)-1 
    res = -1 
    while start <= end:
        mid = end - (end - start)//2 
        if arr[mid] <= x:
            res = mid
            start = mid + 1 
        elif arr[mid] > x:
            end = mid-1 
    return res
    