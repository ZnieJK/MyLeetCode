#Find the Index of the forest Occurrence in a string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
         
        index = haystack.find(needle)
        return index
