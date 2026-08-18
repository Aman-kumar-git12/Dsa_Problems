# Daily Temperatures
# link : https://leetcode.com/problems/daily-temperatures/description/


def dailyTemperatures(self, arr: List[int]) -> List[int]:
    stack = []
    ans = []
    for i in range(len(arr)-1 , -1 , -1):
        if len(stack ) ==0:
            stack.append((arr[i] , i))
            ans.append(-1)
        elif len(stack) != 0 and stack[-1][0] > arr[i]:
            ans.append(stack[-1][1])
            stack.append((arr[i] , i))
        elif len(stack) != 0 and stack[-1][0] <= arr[i]:
            while len(stack) != 0 and stack[-1][0] <= arr[i]:
                stack.pop()
            if len(stack) == 0 :
                stack.append((arr[i] , i))
                ans.append(-1)
            else:
                ans.append(stack[-1][1])
                stack.append((arr[i] , i))
        
    
    ans = ans[::-1]
    print(ans)

    for i in range(len(arr)):
        if ans[i] == -1:
            ans[i] = 0
        else:
            ans[i] = ans[i]-i
    return ans

            

    