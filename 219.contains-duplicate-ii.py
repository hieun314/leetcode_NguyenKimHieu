#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tmp = nums[:k+1]
        if len(tmp) > len(set(tmp)): return True
        for i in range(k+1, len(nums)):
            tmp.pop(0)
            if nums[i] in tmp: return True
            tmp.append(nums[i])
        return False
# @lc code=end

