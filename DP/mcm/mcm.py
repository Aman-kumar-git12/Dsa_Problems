# Question : Matrix chain multiplication
# link : https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
def matrixMultiplication(self, arr):
    # code here
    minans = float('inf')
    dp = [[-1] * len(arr) for i in range(len(arr) )]
    def helper(arr , i , j ):
        
        if i >= j :
            return 0 
        if dp[i][j] != -1:
            return dp[i][j]
            
        minans = float('inf')
        for k in range(i , j):

            tempans  = helper(arr , i , k) + helper(arr , k+1 , j) + (arr[i-1] * arr[k] * arr[j])
            
            if tempans < minans:
                minans = tempans 
                dp[i][j] = tempans
        return dp[i][j]
        
    return helper(arr , 1 , len(arr)-1)
            