class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set()
        inter = set()
        for n in nums1:
            s1.add(n)
        for n in nums2:
            if n in s1:
                inter.add(n)
        return inter
