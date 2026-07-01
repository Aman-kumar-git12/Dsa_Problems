# Question : Ceil in a Sorted Array
# link : https://www.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1

def findCeil(self, arr, x):
    # code here
    res= -1
    start , end = 0 , len(arr)-1 
    while start <= end :
        mid = end - (end- start)//2
        if arr[mid] >= x:
            res = mid 
            end = mid - 1 
        else:
            start = mid + 1 
    return res
