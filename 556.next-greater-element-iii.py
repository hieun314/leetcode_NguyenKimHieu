#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if list(str(n)) == sorted(str(n), reverse = True) : return -1
        n = list(str(n))
        tmp = []
        for i in range(len(n)-1,0,-1):
            tmp.append(n[i])
            if n[i-1] < max(tmp):
                for j in sorted(tmp):
                    if j > n[i-1]:
                        n[i-1],n[-tmp.index(j)-1] = n[-tmp.index(j)-1],n[i-1]
                        n[i:] = sorted(n[i:])
                        break
                break
        a = int(''.join([n[i] for i in range(len(n))]))
        return a if a < 2**31 else -1      
# @lc code=end

