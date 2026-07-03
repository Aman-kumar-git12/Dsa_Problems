# Question : Maximal Rectangle
# link : https://leetcode.com/problems/maximal-rectangle/description/


def maximalRectangle(self, matrix: List[List[str]]) -> int:

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or matrix[i][j] == '0' :
                matrix[i][j] = int(matrix[i][j])
            else:
                matrix[i][j] = int(matrix[i-1][j] ) + int(matrix[i][j])

    def mah(arr):
        leftarr = []
        rightarr = []
        area = []

        stack = []
        for i in range(len(arr)):
            if len(stack) == 0:
                leftarr.append(-1)
                stack.append((arr[i] , i ))
            elif len(stack) > 0 and stack[-1][0] < arr[i]:
                leftarr.append(stack[-1][1])
                stack.append((arr[i] , i ))
            elif len(stack) > 0 and stack[-1][0] >=  arr[i]:
                while len(stack) > 0 and stack[-1][0] >= arr[i]:
                    stack.pop()
                if len(stack) == 0:
                    leftarr.append(-1)
                    stack.append((arr[i] , i ))
                else:
                    leftarr.append(stack[-1][1])
                    stack.append((arr[i] , i ))
        
        stack = []
        for i in range(len(arr)-1 , -1 , -1 ):
            if len(stack) == 0:
                rightarr.append(len(arr) )
                stack.append((arr[i] , i ))
            elif len(stack) > 0 and stack[-1][0] < arr[i]:
                rightarr.append(stack[-1][1])
                stack.append((arr[i] , i ))
            elif len(stack) > 0 and stack[-1][0] >=  arr[i]:
                while len(stack) > 0 and stack[-1][0] >= arr[i]:
                    stack.pop()
                if len(stack) == 0:
                    rightarr.append(len(arr) )
                    stack.append((arr[i] , i ))
                else:
                    rightarr.append(stack[-1][1])
                    stack.append((arr[i] , i ))

        rightarr.reverse()
        # print(leftarr)
        # print(rightarr)
        for i in range(len(leftarr)):
            area.append((rightarr[i] - leftarr[i] - 1 ) * arr[i])
        return max(area)

    # print(matrix)
    maxval = 0 
    for i in range(len(matrix)):
        maxval = max(maxval , mah(matrix[i]))
    return maxval