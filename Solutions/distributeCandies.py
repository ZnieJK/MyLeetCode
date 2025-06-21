class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        temp = set(candyType)
        if (len(candyType)//2) > len(temp):
            return len(temp)
        return len(candyType)//2
