
def inorder(root):
    arr = []
    def helper(node):
        if not node:
            return 
        helper(node.left)
        helper(node.right)
        arr.append(node.val)
    return arr