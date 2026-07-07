# Question : Longest Subarray with Sum K
# link : https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1


def longestSubarray(self, arr, k):  
    n = len(arr)
    i , j = 0 , 0 
    summ = 0 
    length = 0 
    maxlength = 0 
    while j < n :
        summ += arr[j]
        length +=1 
        while summ > k :
            sum-= arr[i]
            length -=1 
            i+=1
            
        
        if summ != k :
            j+= 1
        elif summ == k:
            maxlength = max(maxlength , length) 
            summ-= arr[i]
            length -= 1
            
            i+=1 
            j +=1 
    return maxlength
            