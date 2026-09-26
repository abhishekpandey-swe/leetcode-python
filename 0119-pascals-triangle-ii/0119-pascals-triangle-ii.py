class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        res = [1]
        for k in range(1 , rowIndex + 1):
            res.append(res[-1] * (rowIndex - k + 1) // k)
        return res
        