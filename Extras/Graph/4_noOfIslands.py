
# Quesiton : Number of Islands (DFS)
# link : https://my.newtonschool.co/playground/code/1f4m14i57qrj
def numIslands(grid,n,m):
    directions = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]

    def dfs(row , col):
        grid[row][col] = 0 
        for dx , dy in directions:
            new_row = row + dx 
            new_col = col + dy
            if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 1:
                dfs(new_row , new_col)

    count = 0   

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count+=1 
                dfs(i , j)
    return count 