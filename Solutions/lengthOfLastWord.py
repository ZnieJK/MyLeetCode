class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        temp = s.split()
        return len(temp[-1])
