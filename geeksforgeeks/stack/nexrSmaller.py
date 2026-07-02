# Quesiton : Next Smaller Element
# link : https://www.geeksforgeeks.org/problems/immediate-smaller-element1142/1


def nextSmallerEle(self, arr):
    stack , res = [] , []
    
    for i in range(len(arr)-1 , -1 , -1):
        if len(stack) == 0:
            res.append(-1)
            stack.append(arr[i])
        elif stack[-1] < arr[i]:
            res.append(stack[-1])
            stack.append(arr[i])
        elif stack[-1] >= arr[i]:
            while len(stack) != 0 and stack[-1] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
                stack.append(arr[i])
            else:
                res.append(stack[-1])
                stack.append(arr[i])
# 		print(res)
    finalArr = []
    for i in range(len(res) -1 , -1 , -1 ):
        finalArr.append(res[i])
    return finalArr