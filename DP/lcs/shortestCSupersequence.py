# Quesiton : Shortest Common Supersequence
# link : https://leetcode.com/problems/shortest-common-supersequence/description/

def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    def lcs(s , t):
        
        dp = [[-1] *(len(t) +  1 )for _ in range(len(s) + 1 )]

        for i in range(len(s) + 1):
            for j in range(len(t) + 1 ):
                if i == 0 or j ==0:
                    dp[i][j] = 0 
        
        for i in range(1 , len(s) + 1):
            for j in range(1 , len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
                
        ans = ''
        i , j = len(s) , len(t)
        while i > 0 and j > 0 :
            if s[i-1]== t[j-1]:
                ans+=s[i-1]
                i-=1
                j-=1
            else:
                if dp[i-1][j] >= dp[i][j-1]:
                    ans+=s[i-1]
                    i-=1
                else:
                    ans+=t[j-1]
                    j-=1 
        while i > 0 :
            ans+= s[i-1]
            i-=1
        
        while j > 0 :
            ans+= t[j-1]
            j-=1

        newarr = ''
        for i in range(len(ans)-1 , -1 , -1):
            newarr+=ans[i]
        return newarr 
    lcs = lcs(str1 , str2)
    return lcs 