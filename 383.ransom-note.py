#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        if len(ransomNote) > len(magazine): return False
        else:
            for i in ransomNote:
                if i in magazine:
                    magazine.remove(i)
                else:
                    return False
            return True
# @lc code=end

