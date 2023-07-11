#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def tree(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            if root.left is None:
                return 1 + tree(root.right)
            if root.right is None:
                return 1 + tree(root.left)
            return 1 + min(tree(root.left), tree(root.right))
        return tree(root)     
# @lc code=end

