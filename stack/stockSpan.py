# Question : Stock span problem
# link : https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

def calculateSpan(self, arr):
        # code here
        
        stack , res = [] , []
        
        for i in range(len(arr)):
            if len(stack) == 0 :
                res.append(i-(-1))
                stack.append((arr[i] , i))
                
            elif len(stack) > 0 and stack[-1][0] > arr[i]:
                res.append(i - stack[-1][1])
                stack.append((arr[i] , i))
                
            elif len(stack) > 0 and stack[-1][0] <= arr[i]:
                while len(stack) > 0 and stack[-1][0] <= arr[i]:
                    stack.pop()
                if len(stack) == 0 :
                    res.append(i-(-1))
                    stack.append((arr[i] , i))
                else:
                    res.append(i - stack[-1][1])
                    stack.append((arr[i] , i))
        return res 
        