#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == '}':
                if len(stack) == 0:
                    return False                
                elif stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif char == ']':
                if len(stack) == 0:
                    return False
                elif stack[-1] == '[':
                    stack.pop()
                else:
                    return False                
        return len(stack) == 0   
# @lc code=end

