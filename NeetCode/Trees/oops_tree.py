from collections import deque 

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_from_input():
    data = input("Enter values (use space, 'None' for null): ").split()
    
    # Convert input into list
    arr = [None if x.lower() in ('null' , 'none') else int(x) for x in data]

    if not arr or arr[0] is None:
        return None
    
    root = Tree(arr[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        current = queue.popleft()
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            current.left = Tree(arr[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(arr) and arr[i] is not None:
            current.right = Tree(arr[i])
            queue.append(current.right)
        i += 1
    
    return root


# # use this code to implement the tree_construction 
# from oops_tree import build_tree_from_input
# root = build_tree_from_input()



