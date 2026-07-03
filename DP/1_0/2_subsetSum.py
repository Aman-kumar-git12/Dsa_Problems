# Question : Subset Sum Problem
# Link : https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1



# Recursion 
def helper(i , sum):
    
    if sum == 0 :
        return  True 
    if i == 0 : 
        return False 

    if arr[i-1] <= sum: 
        return  helper(i-1 , sum - arr[i-1])  or helper(i-1 , sum )
    else :
        return   helper(i-1 , sum )
    
return helper(len(arr) , sum)


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



# Tabulation 
for i in range(len(arr) + 1 ):
    for j in range(sum + 1):
        if i == 0 and j ==0 :
            dp[i][j] = True 
        elif i == 0 :
            dp[i][j] = False
        elif j == 0 :
            dp[i][j] = True 
            
for i in range(1 , len(arr) + 1 ):
    for j in range(1 , sum + 1):
        if arr[i-1] <= j:
            dp[i][j] = dp[i-1][j- arr[i-1]] or dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
        
return dp[len(arr)][sum]


