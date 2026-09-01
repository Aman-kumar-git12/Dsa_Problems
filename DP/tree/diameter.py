# Question : Diameter of a tree
# Link : https://www.geeksforgeeks.org/diameter-of-a-binary-tree/



def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    res = 0
    def helper(root):
        nonlocal res 
        if not root:
            return 0 
        left = helper(root.left)
        right = helper(root.right)

        temp =1 + max(left , right)
        ans = left + right
        res = max(ans, res)
        return  temp 
    helper(root)
    return  res 