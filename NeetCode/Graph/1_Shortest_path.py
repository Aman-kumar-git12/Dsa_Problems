# Quesiton : Shortest Path in Binary Matrix
# Link : https://neetcode.io/problems/shortest-path-in-binary-matrix/question

from collections import deque 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0 , 1) , (0 , -1) , (1 , 0) ,(1 , 1) , (1 , -1) , (-1 , 0), (-1 ,1 ) , (-1 , -1)] 

        if grid[0][0] == 1:
            return -1 

        visited = [[0 , 0 , 0 ] for _ in  range(n)]
        
        q = deque([(0 , 0 , 1)])
        visited[0][0] = 1 

        while q:  
            x , y , dist = q.popleft() 

            if x == n-1  and y == n-1:
                return dist

            for dx , dy in directions:
                x_shift = x + dx
                y_shift = y + dy 

                if 0 <= x_shift < n and  0 <= y_shift < n and grid[x_shift][y_shift] == 0  :
                    grid[x_shift][y_shift] = 1 
                    q.append((x_shift , y_shift , dist + 1 ))
        return -1 

            





