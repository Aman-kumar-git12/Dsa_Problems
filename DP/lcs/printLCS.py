# Question : Printing Longest Common Subsequence 
# link : no link 😭

def printLCS(self, s1, s2):
    
    # initialisation 
    dp =[ [-1]* (len(s2)+1) for _ in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i ==0 or j == 0 :
                dp[i][j] = 0 
    
    for i in range(1 , len(s1)+1):
        for j in range(1 , len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    ansarr = []       
    ans = ""
    i  , j= len(s1)   , len(s2) 
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            ans += s1[i-1]
            i-=1
            j-=1
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                i-=1
            else:
                j-=1
                
    newans = ''
    for i in range(len(ans)-1 , -1 , -1):
        newans+= ans[i]
    ansarr.append(newans)
    return ansarr