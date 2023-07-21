#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        list_char = {}
        list_p = {}
        if len(s) < len(p): return []
        for i in range(len(p)):
            if p[i] not in list_p:
                list_p[p[i]] = 1
            else: list_p[p[i]] += 1
        for i in range(len(p)):
            if s[i] not in list_char and s[i] in list_p:
                list_char[s[i]] = 1
            elif s[i] in list_char: list_char[s[i]] += 1
        output = []
        start = 0
        if list_char == list_p: output.append(0)    
        for j in range(len(p), len(s)):
            if s[start] in list_char:
                list_char[s[start]] -= 1
            start += 1
            if s[j] in list_p:
                if s[j] not in list_char: list_char[s[j]] = 1
                else: list_char[s[j]] += 1
                if list_char == list_p: output.append(start)
        return output        
# @lc code=end

