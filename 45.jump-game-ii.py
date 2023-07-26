#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        jump = [float("inf")] * len(nums)
        jump[0] = 0
        for i in range(len(jump)):
            if jump[i] != float("inf"):
                for j in range(i+1, min(nums[i] + i + 1, len(jump))):
                    if jump[j] == float("inf"):
                        jump[j] = jump[i] + 1
                    elif jump[-1] != float("inf"): return jump[-1]
        return jump[-1]
      
# @lc code=end

