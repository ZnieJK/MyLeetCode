class Solution(object):
    def trap(self, height):
        """

        :type height: List[int]
        :rtype: int

        """

        sum = 0
        for i in range(1, len(height)-1):
            right = max(height[:i+1]) if height[:i+1] else 0
            left = max(height[i:]) if height[i:] else 0
            m = min(right, left)
            res = m - height[i]
            sum += res
        return sum
