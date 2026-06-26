from oops_tree import build_tree_from_input
root = build_tree_from_input()


def inorder_traversal(root):
    stack = []
    curr = root
    arr = []
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left 
        else:
            pop_val = stack.pop()
            arr.append(pop_val.val)
            curr  = pop_val.right
    return arr

print(inorder_traversal(root))

