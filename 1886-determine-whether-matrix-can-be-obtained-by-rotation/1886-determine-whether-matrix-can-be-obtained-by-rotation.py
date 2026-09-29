class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        
        n = len(mat)

        # Check whether current matrix equals target

        for _ in range(4):

            if mat == target:
                return True

            for i in range(n):
               for j in range(i , n):
                   mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]

            for i in range(n):
                mat[i].reverse()

        return False