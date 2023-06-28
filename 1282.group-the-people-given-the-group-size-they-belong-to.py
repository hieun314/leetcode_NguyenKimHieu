#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        arr_set = set(groupSizes)
        group = []
        for arr in arr_set:
            search = []
            for j in range(len(groupSizes)):
                if groupSizes[j] == arr:
                    search.append(j)
                    if len(search) % arr == 0: 
                        group.append(search)
                        search = []
        return group
# @lc code=end

