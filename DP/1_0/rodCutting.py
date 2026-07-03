
# Question : Rod Cutting
# Link : https://www.geeksforgeeks.org/rod-cutting-problem-dp-13/


# Memoization 
def cutRod(self, price):
    dp = [[-1] * (len(price) + 1) for _ in range(len(price) + 1 )]
    
    def helper(i , length):
        if i == 0:
            return 0 
        if length == 0:
            return 0 
        if dp[i][length] != -1:
            return dp[i][length]
        if i <= length:
            pick = price[i-1] + helper(i , length - i)
        else:
            pick = helper(i-1 , length)
            
        notpick =  helper(i-1 , length)
        
        dp[i][length] =  max(pick , notpick)
        return dp[i][length]
        
    return helper(len(price) , len(price))
        
    
# Tabulation 
    for i in range(len(price) + 1):
        for j in range(len(price) + 1):
            if i == 0 or j== 0:
                dp[i][j] = 0 
    
    for i in range(1 , len(price) + 1 ):
        for j in range(1 , len(price) +1 ):
            if i <= j:
                dp[i][j] = max( price[i-1] + dp[i][j-i] , dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(price)][len(price)]