
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
       
        x = ''

        for i in range(len(s)):
            if s[i].isalnum():
                x += s[i]
        x = x.lower()
        return(x == x[::-1])