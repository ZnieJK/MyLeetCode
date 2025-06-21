class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visit = set()
        for i in nums:
            if i in visit:
                return True
            visit.add(i)
        return False