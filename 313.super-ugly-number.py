#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        list_num = {}
        for num in primes:
            list_num[num] = 0
        nums = [1]
        for i in range(1, n):
            a = 0
            b = 0
            for j in list_num:
                if a > nums[list_num[j]] * j:
                    a = nums[list_num[j]] * j
                elif a == 0:
                    a = nums[list_num[j]] * j
            for j in list_num:
                if a == nums[list_num[j]] * j:
                    list_num[j] += 1
            nums.append(a)
        print(nums)
        return nums[-1]     
# @lc code=end

