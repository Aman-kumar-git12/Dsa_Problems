# Questoin : Coin Change
# link : https://leetcode.com/problems/coin-change/description/


memoization 
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [[-1]* (amount+ 1) for _ in range(len(coins) + 1 )]
    def helper(i , amount):
        if amount == 0:
            return 0 
        if i == 0:
            return float('inf')

        if dp[i][amount] != -1:
            return dp[i][amount] 
        if coins[i-1] <= amount:
            pick = 1 + helper(i , amount -  coins[i-1])
        else:
            pick = helper(i - 1 , amount)

        notpick = helper(i - 1 , amount)
    
        dp[i][amount] =  min(pick , notpick)
        return dp[i][amount]
    ans = helper(len(coins) , amount) 


# Tabulation (Top-down)
def coinChange(self, coins: List[int], amount: int) -> int:

    dp = [[-1]* (amount + 1) for _ in range(len(coins) + 1 )]
    for i in range(len(coins) + 1):
        for j in range(amount + 1 ):
            if i == 0 and j ==0:
                dp[i][j] = 0 
            elif i == 0:
                dp[i][j] = float('inf') 
            elif j == 0:
                dp[i][j] = 0

    for i in range(1 , len(coins) + 1 ):
        for j in range(1 , amount + 1 ):
            if coins[i-1] <= j:
                dp[i][j] = min(1 + dp[i][j-coins[i-1]] ,dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    if dp[len(coins)][amount] == float('inf'):
        return -1 

    return dp[len(coins)][amount]











        