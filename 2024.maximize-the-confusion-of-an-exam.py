#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def test(char, k):
            s = 0
            max1=0
            for i in range(len(answerKey)):
                if answerKey[i] != char:
                    k -= 1
                while k < 0:
                    if answerKey[s] != char:
                        k += 1
                    s += 1
                max1 = max(max1,i-s+1)
            return max1
        return max(test("F",k),test("T", k))  
# @lc code=end

