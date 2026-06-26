def postorder(root):
    arr = []
    def helper(node):
        if not root:
            return 
        helper(node.left)
        helper(node.right)
        arr.append(node.val)
    return arr