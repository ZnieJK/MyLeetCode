class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while n:
            n -= 1
            ch = n%26
            ans.append( chr(ch + ord('A')) )
            n = n//26
        return "".join(reversed(ans))
