# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            nonlocal diff
            if not root:
                return 0

            l_height = maxDepth(root.left)
            r_height = maxDepth(root.right)

            diff = max(diff, abs(l_height - r_height))

            return max(l_height, r_height) + 1

        maxDepth(root)
        return diff <= 1
