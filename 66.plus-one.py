#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: digits[-1] +=1
        else:
            carry = 1
            i = len(digits)
            while carry != 0:
                if i <= 0: 
                    digits.insert(0, 1)
                    carry = 0
                else:
                    total = digits[i-1] + carry
                    digits[i-1] = total%10                
                    carry = total//10
                    i -= 1
        return digits
        
# @lc code=end

