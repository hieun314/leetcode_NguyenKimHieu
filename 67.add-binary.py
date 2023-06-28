#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a) + int(b)
        c=str(c)
        carry = 0
        output = ""
        for i in range(1, len(c) + 1):
            if int(c[-i]) + carry == 0:
                output += "0"
                carry = 0            
            elif int(c[-i]) + carry == 1: 
                output += "1"
                carry = 0
            elif int(c[-i]) + carry == 2: 
                output += "0"
                carry = 1
            elif int(c[-i]) + carry == 3:
                output += "1"
                carry = 1          
        if carry == 1: output += "1"
        output = output[::-1]
        return output
# @lc code=end

