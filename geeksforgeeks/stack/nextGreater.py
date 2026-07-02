# Quesiton : Next Greater Element
# link : https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1

def nextLargerElement(self, arr):
    # code here
    res = []
    stack = []
    
    for i in range(len(arr)-1 , -1 , -1):
        if len(stack) == 0 :
            res.append(-1)
            stack.append(arr[i])
        elif len(stack) >0 and stack[-1] > arr[i]:
            res.append(stack[-1])
            stack.append(arr[i])
        elif len(stack) > 0 and stack[-1] <= arr[i]:
            while len(stack) > 0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
                stack.append(arr[i])
            else:
                res.append(stack[-1])
                stack.append(arr[i])
    
    
    newArr = []
    ele = len(res)-1
    while  ele >= 0 :
        newArr.append(res[ele])
        ele -=1
    return newArr
                