class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        temp = []

        for i in score:
            temp.append(i)
        temp.sort()
        temp.reverse()
       
        rank = len(score)
        ans = [""] * rank


        for i in range(rank):
            if i == 0:
                res = "Gold Medal"
            elif i == 1:
                res = "Silver Medal"
            elif i == 2:
                res = "Bronze Medal"
            else:
                res = "" + str(i+1)
            idx = score.index(temp[i])
            ans[idx] = res
        return ans
