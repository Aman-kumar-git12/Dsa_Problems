# Question : Index of first 1 in a sorted array of 0s and 1s
# link : https://www.geeksforgeeks.org/problems/index-of-first-1-in-a-sorted-array-of-0s-and-1s4048/1

def firstIndex(self, arr):
    # Your code goes here

    start , end = 0 , len(arr)-1
    res = -1 
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == 1:
            res  = mid
            end = mid -1 
        else :
            start= mid + 1
    return res 