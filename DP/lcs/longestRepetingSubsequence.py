
# Question : Longest Repeating Subsequence
# link : https://www.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1


def LongestRepeatingSubsequence(self, s):
    # subsequence which is repeting alteast onece
    dp = [[-1] * (len(s) + 1 ) for _ in range(len(s) + 1)]
    def helper(i , j):
        if i == 0 or j ==0 :
            return 0 
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i-1] == s[j-1] and i!= j:
            dp[i][j] =  1 + helper(i -1 , j-1 )
        else:
            dp[i][j] =  max(helper(i-1 , j) , helper(i , j-1))
        return dp[i][j]
        
    return helper(len(s) , len(s))


    # Tabulation
    for i in range (len(s) +1 ):
        for j in range(len(s) + 1):
            if i ==0 or j == 0 :
                dp[i][j] = 0 
                
    for i in range (1 , len(s) +1 ):
        for j in range(1 , len(s) + 1):
            if s[i-1] == s[j-1] and i!=j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    return dp[len(s)][len(s)]
