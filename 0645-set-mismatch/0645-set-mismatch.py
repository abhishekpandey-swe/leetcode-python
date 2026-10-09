class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:

        n = len(nums)

        # 1. Calculate expected sum from 1 to n.

        expected_sum = n * (n + 1) // 2
        expected_sum_sq = n * (n + 1) * (2 * n + 1) // 6

        # 2. Calculate the actual sum from input array.

        actual_sum = sum(nums)
        actual_sum_sq = sum(x * x for x in nums)

        # 3. Set-up equation
        # Missing_no = X , Repeating_no = Y

        # difference1 = Y - X
        diff1 = actual_sum - expected_sum

        # difference2 = Y² - X²
        diff2 = actual_sum_sq - expected_sum_sq

        # 4. Solve for Y and X
        # Y² - X² = (Y - X)(Y + X)
        # diff2 = diff1 * (Y + X)
        # sum_xy = Y + X

        sum_xy = diff2 // diff1

        # Y = ((Y - X) + (Y + X)) / 2

        duplicate = (diff1 + sum_xy) // 2

        # X = ((Y + X) - (Y - X)) / 2

        missing = (sum_xy - diff1) // 2

        return [duplicate, missing]










        