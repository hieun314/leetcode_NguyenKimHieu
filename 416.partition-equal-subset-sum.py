#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 != 0: return False
        target = s // 2
        sum_arr = set()
        total = 0
        for num in nums:
            tmp = sum_arr.copy()
            for i in tmp:
                sum_arr.add(i+num)
            sum_arr.add(num)
            if target in sum_arr: return True
        return False 
# @lc code=end

