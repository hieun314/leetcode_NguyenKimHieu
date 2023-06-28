#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = []
        output = []
        arr=list(set(nums))
        for i in range(len(arr)):
            temp.append(nums.count(arr[i]))
            output.append(arr[i])
            if len(temp) > k:
                output.pop(temp.index(min(temp)))                
                temp.remove(min(temp))
        return output

# @lc code=end

