# Question : Minimum Allocation of Pages
# link : https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1


def findPages(self, arr, k):
    
    # code here
    if len(arr) < k:
        return -1 
    
    start , end = max(arr) , sum(arr)
    
    res = -1 
    
    def isValid(arr , n  , k , maxval):
        students = 1 
        summ = 0 
        for i in range(n):
            summ+= arr[i]
            if summ > maxval:
                students += 1
                summ = arr[i]
        return students <= k 
        
    while start <= end:
        mid = end-(end-start)//2 
        
        if isValid(arr , len(arr) , k , mid):
            res = mid 
            end = mid -1 
        else:
            start = mid + 1
        
    return res 
