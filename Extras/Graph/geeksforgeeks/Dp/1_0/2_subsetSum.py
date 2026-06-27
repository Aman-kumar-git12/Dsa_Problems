# Question : Subset Sum Problem
# Link : https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1



# memoization 

dp = [[-1] * (sum+ 1) for i in range(len(arr) + 1)]
def helper(i , sum):
    
    if sum == 0 :
        return  True 
    if i == 0 : 
        return False 
    
    if dp[i][sum] != -1:
        return dp[i][sum]
    if arr[i-1] <= sum: 
        
        dp[i][sum] =  helper(i-1 , sum - arr[i-1])  or helper(i-1 , sum )
    else :
        dp[i][sum] =  helper(i-1 , sum )
        
    return dp[i][sum]
    
return helper(len(arr) , sum)


