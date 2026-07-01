# Question : Search in infinite sorted array

def searchInInfiniteSortedArray(self, arr, target):

    def binarySearch( arr , start, end , target ):
        while start <= end:
            mid = end - (end - start)//2 
            if arr[mid] == target:
                return mid 
            elif arr[mid] < target:
                start = mid + 1 
            else:
                end = mid - 1 
        return -1
    
    start , end = 0 , 1 
    while arr[end] < target:
        start = end  + 1
        end = end * 2 
    return binarySearch(arr , start , end , target)
    