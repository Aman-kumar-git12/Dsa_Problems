# Question : Search a 2D Matrix
# link : https://leetcode.com/problems/search-a-2d-matrix/


def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    # # brute force
    # for i in range(len(matrix)):
    #     for j in matrix[i]:
    #         if j == target:
    #             return True 
    # return False

    m ,n = len(matrix) , len(matrix[0])
    start , end = 0 , (m)*(n) - 1

    while start <= end:
        mid = (start + end )//2

        # divide into n parts 
        row = mid // n 
        # remaining of n parts
        col = mid % n 
        
        if matrix[row][col] == target:
            return True 
        elif matrix[row][col] > target:
            end = mid -1 
        else:
            start = mid +1 
    return False