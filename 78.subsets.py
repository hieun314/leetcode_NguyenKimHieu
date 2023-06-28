#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
def solve(i, curr, nums, ans):
    if i >= len(nums):
        ans.append(curr.copy())
        return ans
    curr.append(nums[i])
    solve(i+1, curr, nums, ans)
    curr.pop()
    solve (i+1, curr, nums, ans)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        solve(0, [], nums, ans)
        return ans
# @lc code=end

