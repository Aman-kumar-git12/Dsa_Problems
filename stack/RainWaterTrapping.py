# Question : Trapping Rain Water
# link : https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1
def maxWater(self, arr):
    # code here
    left , right = [0]*len(arr) , [0]*len(arr)
    left[0] = arr[0]
    right[len(arr)-1] = arr[len(arr)-1]
    for i in range(1, len(arr)):
        left[i] = max(left[i-1] , arr[i] )
    
    for i in range(len(arr)-2 , -1 , -1):
        right[i] = max(right[i+1] , arr[i])
    
    total = [0]* len(arr)
    for i in range(1 , len(arr)-1):
        total[i] = min(left[i] , right[i]) - arr[i]

    return sum(total)
            