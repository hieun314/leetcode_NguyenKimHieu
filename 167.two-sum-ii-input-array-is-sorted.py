#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while True:
            mid = (r+l)//2
            a = numbers[l] + numbers[r]
            b = numbers[mid] + numbers[r]
            c = numbers[l] + numbers[mid]
            if a == target:
                return[l+1,r+1]
            elif b == target:
                return [mid+1,r+1]
            elif c == target:
                return [l+1, mid+1]
            if c > target:
                r = mid
            elif b < target:
                l = mid
            elif a > target:
                r -= 1
            elif a < target:
                l += 1      
# @lc code=end

