# Question : 0 - 1 Knapsack Problem
# Link : https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

# Recursion 
def knapsack(self, W, value, wt):
    def helper(i , W):
        # base case
        if W == 0  or  i <  0  :
            return 0 
        
        pick = 0 
        if wt[i]  <= W:
            pick = value[i] + helper(i-1 , W - wt[i])
            
        notpick = helper(i-1 , W)
        
        return max(pick , notpick)
        
    return helper(len(wt)-1 , W)

# Memoziation 
def knapsack(self, W, value, wt):
    dp = [[-1] * (W+ 1) for _ in range(len(wt) )]
    def helper(i , W):
        # base case
        if W == 0  or  i <  0  :
            return 0 
        
        if dp[i][W] != -1 :
            return dp[i][W]
        
        pick = 0 
        if wt[i]  <= W:
            pick = value[i] + helper(i-1 , W - wt[i])
            
        notpick = helper(i-1 , W)
        
        dp[i][W] =  max(pick , notpick)
        
        return dp[i][W]
        
    return helper(len(wt)-1 , W)

# Tabulation (Top-down)

dp = [[-1]* (W + 1) for _ in range(len(wt) + 1)]

for i in range(len(wt) + 1):
    for j in range(W +1):
        if i == 0 or j == 0 :
            dp[i][j] = 0 


for i in range(1 , len(wt) + 1):
    for j in range(1 , W + 1 ):
        if wt[i-1] <= j: 
            dp[i][j] = max(value[i-1] + dp[i-1][j - wt[i-1]] , dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

return dp[len(wt)][W]



