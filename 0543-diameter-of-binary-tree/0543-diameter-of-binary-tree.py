# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0

        def depth(root):
            nonlocal diam
            if not root:
                return 0

            leftree = depth(root.left)
            rightree = depth(root.right)

            diam = max(diam, leftree + rightree)
            return max(leftree, rightree) + 1

        depth(root)

        return diam
