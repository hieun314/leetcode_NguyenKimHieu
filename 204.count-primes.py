#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [True] * n
        if n > 0: nums[0] = False
        if n > 1: nums[1] = False
        for i in range(2, n - 1):
            if nums[i] == True:
                for j in range(i*i, n , i):
                    nums[j] = False
        return nums.count(True)
# @lc code=end

