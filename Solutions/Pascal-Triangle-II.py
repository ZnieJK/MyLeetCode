#Pascal’s Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
       
        prevRow = self.getRow(rowIndex - 1)
        newRow = [1] * (rowIndex+1)


        for i in range(1, rowIndex):
            newRow[i] = prevRow[i-1] + prevRow[i]


        return newRow