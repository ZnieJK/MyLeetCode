class Solution:
    def addSpace(n, s):
        return ' ' * n + s


    def spiral(n):
        if n == 1:
            return [['1']]


        newMatrix = [[-1 for i in range(n)] for j in range(n)]
        oldMatrix = spiral(n-1)


        for row in range(n-1):
            for col in range(n-1):
                if n % 2 == 0:
                    newMatrix[row][col] = addSpace(len(str(n*n)) - len(str(oldMatrix[row][col])), str(oldMatrix[row][col]))
                if n % 2 == 1:
                    newMatrix[row+1][col+1] = addSpace(len(str(n*n)) - len(str(oldMatrix[row][col])), str(oldMatrix[row][col]))


        
        if n % 2 == 0:
            k = (n-1) ** 2 + 1
            r = 0
            c = n - 1
            while(True):
                newMatrix[r][c] = addSpace(len(str(n*n)) - len(str(k)), str(k))
                k = k + 1
                if r != n - 1:
                    r = r + 1
                else:
                    c = c - 1
                if k == n ** 2 + 1:
                    break


        else:
            k = (n-1) ** 2 + 1
