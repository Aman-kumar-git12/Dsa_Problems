# Valid Parentheses
# link : https://leetcode.com/problems/valid-parentheses/description/


def isValid(self, s: str) -> bool:
    stack = []  
    for i in range(len(s)):
        if s[i] == '{' or s[i]=="(" or s[i] == '[':
            stack.append(s[i])
        elif s[i] == '}':
            if len(stack) == 0:
                return False
            elif stack[-1] != '{':
                return False 
            else:
                stack.pop()
        elif s[i] == ']':
            if len(stack) == 0:
                return False
            elif stack[-1] != '[':
                return False 
            else:
                stack.pop()
        
        elif s[i] == ")":
            if len(stack) == 0:
                return False
            elif stack[-1] != '(':
                return False 
            else:
                stack.pop()
    if len(stack) == 0:
        return True 

    return False 

    