
# Question : Maximum Path Sum in a Binary Tree
# Link : https://leetcode.com/problems/binary-tree-maximum-path-sum/description/


def maxPathSum(self, root: Optional[TreeNode]) -> int:
    res = float('-inf')
    def helper(node ):
        nonlocal res
        # base case
        if not node : return 0
        
        # hypothesis 
        left = helper(node.left )
        right = helper(node.right)

        # induction 
        temp = max(max(left , right) + node.val , node.val)
        ans  = max(temp , node.val + left + right)
        res = max(ans , res)
        return temp
    helper(root)
    return res