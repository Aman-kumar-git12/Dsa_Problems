

# Quesiton : Max Sum Subarray of size K
# link : https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1



def maxSubarraySum(self, arr, k):
    # simple code 
    summ = sum(arr[:k])
    maxsum = summ
    for i in range(k , len(arr)):
        summ += arr[i]
        summ -= arr[i-k]
        maxsum = max(summ , maxsum)
    return maxsum
    

    # sliding code 
    i , j = 0 , 0
    summ = 0 
    maxsumm = 0 
    while j < len(arr) :
        # calculation 
        summ += arr[j]
        if (j - i + 1) < k:
            j+=1 
        else:
            # ans  
            maxsumm = max(summ , maxsumm)
            summ -= arr[i]
            # sliding 
            i+=1
            j+=1 
    return maxsumm 
                