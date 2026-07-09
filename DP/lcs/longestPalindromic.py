# Quesiton :  Longest Palindromic Subsequence
# link :https://leetcode.com/problems/longest-palindromic-subsequence/description/

def longestPalindromeSubseq(self, s: str) -> int:
    dp = [[0] * len(s) for _ in range(len(s) )]
    # def helper(i , j):
    #     if i == j :
    #         return 1 
    #     if i > j:
    #         return 0 
    #     if dp[i][j] != -1 :
    #         return dp[i][j]
        
    #     if s[i-1] == s[j-1]:
    #         dp[i][j] =  2 + helper(i+1 , j-1)
    #     else:
    #         right  = helper(i+1 , j)
    #         left = helper(i , j-1)

    #         dp[i][j]  =  max(right , left)
    #     return dp[i][j]
    
    # return helper(1 , len(s))

    n = len(s)
    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
