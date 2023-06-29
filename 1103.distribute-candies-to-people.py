#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output=[0]*num_people
        i = 0
        k = 1
        while candies != 0:
            if candies < k:
                output[i] += candies
                break
            output[i] += k
            candies -= k
            i += 1
            k += 1
            if i == num_people: i = 0
        return output
# @lc code=end

