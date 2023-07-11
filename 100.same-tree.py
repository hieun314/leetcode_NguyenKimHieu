#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def test(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            if p.val != q.val: return False
            return test(p.left,q.left)  and test(p.right,q.right)
        return test(p, q)        
# @lc code=end

