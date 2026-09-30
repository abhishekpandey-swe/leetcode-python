class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        columns = len(matrix[0])

        # Step 1: Check whether the first column contains a zero.

        first_column_zero = False 

        for i in range(rows):
            if matrix[i][0] == 0:
                first_column_zero = True
                break

        # Step 2: Check whether the first row contains a zero.

        first_row_zero = False

        for j in range(columns):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        
        # Step 3: Use the first row and first column as markers.
        for i in range(1, rows):
            for j in range(1, columns):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 4: Use the first column markers to zero rows.
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, columns):
                    matrix[i][j] = 0

        # Step 5: Use the first row markers to zero columns.
        for j in range(1, columns):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Step 6: Handle the original first row.
        if first_row_zero:
            for j in range(columns):
                matrix[0][j] = 0

        # Step 7: Handle the original first column.
        if first_column_zero:
            for i in range(rows):
                matrix[i][0] = 0

        



        




             
        