from oops_tree import build_tree_from_input
root = build_tree_from_input()

def preorder(root):
    arr = []
    def helper(node):
        if not node:
            return 
        arr.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return arr

print("Preorder Traversal:", preorder(root))