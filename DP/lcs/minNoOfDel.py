# Question : Minimum number of deletions
# link : https://www.geeksforgeeks.org/problems/minimum-number-of-deletions4610/1


def minDeletions(self, s):
    # # one way 
    # dp = [[-1] *( len(s) + 1) for _ in range(len(s) + 1)]
    # def helper(i , j ):
    #     if i >= j:
    #         return 0
    #     if dp[i][j] != -1:
    #         return dp[i][j]
            
    #     if s[i-1]== s[j-1]:
    #         dp[i][j] =  helper(i+1 , j-1)
    #     else:
    #         left = 1 + helper(i+1 , j)
            
    #         right = 1 + helper(i , j-1)
    #         dp[i][j] =  min(left , right)
    #     return dp[i][j]   
    # return helper(1 , len(s))
    
    dp = [[0]*(len(s)+1)  for _ in range(len(s)+1)]
    
    for i in range(len(s) , -1 , -1):
        for j in range(i+1 , len(s) + 1):
            if s[i-1] == s[j-1]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(1 + dp[i+1][j] ,  1 + dp[i][j-1])
    return dp[1][len(s)]



