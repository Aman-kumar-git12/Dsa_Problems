# Question : Get Min from Stack 
# link : https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1


# tc = O(n) sc = O(1)
class SpecialStack:

    def __init__(self):
        # Define Stack
        self.stack = []
        
    
    def push(self, x):
        # Add an element to the top of Stack
        self.stack.append(x)

    
    def pop(self):
        # Remove the top element from the Stack
        self.stack.pop()

    
    def peek(self):
        # Returns top element of Stack
        if len(self.stack)==0:
            return -1
        return self.stack[-1]
        
    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack)==0

    
    def getMin(self):
        # Finds minimum element of Stack
        if len(self.stack)==0:
            return -1
        return min(self.stack)


# tc - O(1)  , sc - O(n)

class SpecialStack:

    def __init__(self):
        # Define Stack
        self.stack = []
        self.newstack = []
        
    
    def push(self, x):
        # Add an element to the top of Stack
        self.stack.append(x)
        
        if len(self.newstack) != 0:
            self.newstack.append(min(x, self.newstack[-1]))
        else:
            self.newstack.append(x)
            
            
          
        

    
    def pop(self):
        # Remove the top element from the Stack
        self.stack.pop()
        self.newstack.pop()

    
    def peek(self):
        # Returns top element of Stack
        if len(self.stack)==0:
            return -1
        return self.stack[-1]
        
    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack)==0

    
    def getMin(self):
        # Finds minimum element of Stack
        if len(self.stack)==0:
            return -1
        return self.newstack[-1]


# tc -> O(1) , sc -> O(1)

class SpecialStack:

    def __init__(self):
        # Define Stack
        self.stack = []
        
    
    def push(self, x):
        # Add an element to the top of Stack
        self.stack.append(x)

    
    def pop(self):
        # Remove the top element from the Stack
        self.stack.pop()

    
    def peek(self):
        # Returns top element of Stack
        if len(self.stack)==0:
            return -1
        return self.stack[-1]
        
    def isEmpty(self):
        # Check if the stack is empty
        return len(self.stack)==0

    
    def getMin(self):
        # Finds minimum element of Stack
        if len(self.stack)==0:
            return -1
        return min(self.stack)