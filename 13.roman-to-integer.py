#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        i = 0
        while i < len(s):
            if s[-1] == 'I':
                value += 1
                s = s[:-1]
            elif s[-1] == 'V':
                if len(s) > 1 and s[-2] == 'I':
                    value += 4
                    s = s[:-2]
                else:
                    value += 5
                    s = s[:-1]
            elif s[-1] == 'X':
                if len(s) > 1 and s[-2] == 'I':
                    value += 9
                    s = s[:-2]
                else:
                    value += 10
                    s = s[:-1]
            elif s[-1] == 'L':
                if len(s) > 1 and s[-2] == 'X':
                    value += 40
                    s = s[:-2]
                else:
                    value += 50
                    s = s[:-1]
            elif s[-1] == 'C':
                if len(s) > 1 and s[-2] == 'X':
                    value += 90
                    s = s[:-2]
                else:
                    value += 100
                    s = s[:-1]
            elif s[-1] == 'D':
                if len(s) > 1 and s[-2] == 'C':
                    value += 400
                    s = s[:-2]
                else:
                    value += 500
                    s = s[:-1]
            elif s[-1] == 'M':
                if len(s) > 1 and s[-2] == 'C':
                    value += 900
                    s = s[:-2]
                else:
                    value += 1000
                    s = s[:-1]
        return value

# @lc code=end

