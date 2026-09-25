class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []

        if numRows == 0:
            return []

        first_row = [1]
        result.append(first_row)

        if numRows == 1:
            return result 

        for i in range(1 , numRows):
            prev_row = result[i-1]
            row = []

            row.append(1)

            for j in range(i - 1):
                row.append(prev_row[j] + prev_row[j+1])

            row.append(1)

            result.append(row)

        return result

        









   