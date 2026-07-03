# Question : Largest Rectangle in Histogram
# link : https://leetcode.com/problems/largest-rectangle-in-histogram/description/


def largestRectangleArea(self, heights: List[int]) -> int:
    leftindex = []
    rightindex  = []
    area = []

    stack = []
    # nearest smaller to left
    for i in range(len(heights)):
        if len(stack) == 0 :
            stack.append((heights[i] , i))
            leftindex.append(-1)
        elif len(stack) > 0 and stack[-1][0] < heights[i]:
            leftindex.append(stack[-1][1])
            stack.append((heights[i] , i))
        elif len(stack) > 0 and stack[-1][0] >=  heights[i]:
            while len(stack) > 0 and stack[-1][0] >=  heights[i]:
                stack.pop()
            if len(stack) ==0 :
                stack.append((heights[i] , i))
                leftindex.append(-1)
            else:
                leftindex.append(stack[-1][1])
                stack.append((heights[i] , i))

    # nearest smaller to right
    stack = []
    for i in range(len(heights)- 1 , -1 , -1 ):
        if len(stack) == 0 :
            stack.append((heights[i] , i))
            rightindex.append(len(heights))
        elif len(stack) > 0 and stack[-1][0] < heights[i]:
            rightindex.append(stack[-1][1])
            stack.append((heights[i] , i))
        elif len(stack) > 0 and stack[-1][0] >=  heights[i]:
            while len(stack) > 0 and stack[-1][0] >=  heights[i]:
                stack.pop()
            if len(stack) ==0 :
                stack.append((heights[i] , i))
                rightindex.append(len(heights))
            else:
                rightindex.append(stack[-1][1])
                stack.append((heights[i] , i))
    rightindex.reverse()

    for i in range(len(leftindex)):
        area.append((rightindex[i]-leftindex[i]-1) * heights[i])
    # print(leftindex)
    # print(rightindex)
    return max(area) 