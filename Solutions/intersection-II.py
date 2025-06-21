# Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays 
# and you may return the result in any order.


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = Counter(nums1)
        b = Counter(nums2)
        l = []
        for i in a:
            if b.get(i) is not None:
                l+=((min(b[i],a[i]))* [i])
        return l
