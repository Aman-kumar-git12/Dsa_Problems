# Minimum Add to Make Parentheses Valid
# link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/


def minAddToMakeValid(self, s: str) -> int:
    required = 0
    stack = []    
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])    
        elif s[i] == ')':
            if len(stack)==0:
                required+=1 
            else:
                stack.pop()
    while len(stack)!=0:
        required +=1 
        stack.pop()
    return required