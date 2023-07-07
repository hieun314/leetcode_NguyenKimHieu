#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr_set = sorted(list(set(arr1)))
        output = []
        for i in arr2:
            if i in arr_set:
                output.extend([i for _ in range(arr1.count(i))])
                arr_set.remove(i)
        for j in arr_set:
            output.extend([j for _ in range(arr1.count(j))])
        return output     
# @lc code=end

