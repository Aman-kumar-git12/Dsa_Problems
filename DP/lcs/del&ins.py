

# Question : Minimum number of deletions and insertions
# link : https://www.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1

def minOperations(self, s1, s2):
    dp = [[-1]*(len(s2) + 1) for _ in range(len(s1) + 1)]
    def helper(i , j):
        if i == 0:
            return j

        if j == 0:

            return i
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i-1] == s2[j-1]:
            dp[i][j] = helper(i-1 , j-1)
        else:
            remove = 1 + helper(i-1 , j)
            insertion = 1 + helper(i , j-1)
            
            dp[i][j] = min(remove , insertion)
            
        return dp[i][j]

    return helper(len(s1) , len(s2))



    # tabulation 
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1 ):
            if i ==0:
                dp[i][j] = j
            elif j ==0:
                dp[i][j] = i
    
    for i in range(1 , len(s1) + 1):
        for j in range(1 , len(s2) +1 ):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(1 + dp[i-1][j] , 1+ dp[i][j-1])
    return dp[len(s1)][len(s2)]
    
    
    
    