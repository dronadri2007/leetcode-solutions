class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        b = len(a[-1])
        return b
        