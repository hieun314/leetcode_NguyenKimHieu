#
# @lc app=leetcode id=1952 lang=python3
#
# [1952] Three Divisors
#

# @lc code=start
class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 2: return False
        for i in range(3,int(n**0.5)):
            if n%i == 0:
                return False
        if n%(n**0.5) == 0: return True
        return False  
# @lc code=end

