# Question : Longest Common Substring
# link : https://www.geeksforgeeks.org/problems/longest-common-substring1452/1

def longCommSubstr(self , text1 , text2):
    dp = [[-1] * (len(text2)+ 1 ) for _ in range(len(text1) + 1)]
    maxlength = 0 
    # def helper(i , j , count ):
        
    #     if i == 0 or j ==0:
    #         return count

    #     # if dp[i][j] != -1:
    #     #     return dp[i][j]

    #     if text1[i-1] == text2[j-1]:
    #         return helper(i -1  , j-1 , count +1 )
    #     else:
    #         return max(count , helper(i -1  , j , 0) , helper(i  , j-1 , 0))

        

    # return helper(len(text1) , len(text2) , maxlength)
    
    for i in range(len(text1) + 1):
        for j in range(len(text2) + 1):
            if i==0 or j ==0:
                dp[i][j] = 0 
    res  = 0 
    for i in range(1 , len(text1) + 1  ):
        for j in range(1 , len(text2)  + 1):

            if text1[i-1]== text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                res = max(res , dp[i][j])
            else :
                dp[i][j] = 0
    
    return res