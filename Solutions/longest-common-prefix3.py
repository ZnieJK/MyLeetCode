class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        k = 0
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                k +=1
            else:
                break

        return strs[0][:k] if k > 0 else ""
