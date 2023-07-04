#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        note = {"2":"abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        output = []
        if len(digits) > 0:
            for i in note[digits[0]]:
                if len(digits) == 1:
                    output.append(i)
                else:
                    for j in note[digits[1]]:
                        if len(digits) == 2:
                            output.append(i+j)
                        else:
                            for k in note[digits[2]]:
                                if len(digits) == 3:
                                    output.append(i+j+k)
                                else:
                                    for h in note[digits[3]]:
                                        output.append(i+j+k+h)
        return output   
# @lc code=end

