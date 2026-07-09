# Question : Coin Change II
# link : https://leetcode.com/problems/coin-change-ii/description/

# Memoization 
def change(self, amount: int, coins: List[int]) -> int:
    dp = [[-1]* (amount+ 1) for _ in range(len(coins) + 1 )]
    def helper(i , amount):
        if amount == 0:
            return 1
        if i == 0:
            return 0

        if dp[i][amount] != -1:
            return dp[i][amount] 
        
        if coins[i-1] <= amount:
            pick = helper(i , amount -  coins[i-1])
        else:
            pick = 0
            
        notpick = helper(i - 1 , amount)
    
        dp[i][amount] =  pick + notpick
        return dp[i][amount]
    return helper(len(coins) , amount)


# Tabulation (Top-down)
def change(self, amount: int, coins: List[int]) -> int:

    dp = [[-1]* (amount+ 1) for _ in range(len(coins) + 1 )]
    for i in range(len(coins) +1 ):
        for j in range(amount + 1 ):
            if i == 0 and j ==0:
                dp[i][j] = 0 
            elif i == 0 :
                dp[i][j] = 0
            elif j ==0 :
                dp[i][j] = 1 
        
    for i in range(1 , len(coins) + 1):
        for j in range(1 , amount + 1 ):
            if coins[i-1] <= j:
                dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
            else :
                dp[i][j] = dp[i-1][j] 
    return dp[len(coins)][amount]
