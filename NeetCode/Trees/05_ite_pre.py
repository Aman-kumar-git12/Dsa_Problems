
def iterative_preorder(root):
    stack = [root]
    arr = []
    while stack:
        pop_val = stack.pop()
        arr.append(pop_val)  

        if pop_val.right:
            stack.append(pop_val.right) 
        if pop_val.left:
            stack.append(pop_val.left)      
    return arr     
