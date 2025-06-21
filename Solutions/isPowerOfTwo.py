class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n == 1):
            return True
        # y = b^x -> x = logb y
        return math.log2(n) % 1 == 0
