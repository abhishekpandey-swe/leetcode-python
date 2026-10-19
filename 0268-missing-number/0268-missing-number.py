class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        n = len(nums)
        actual_sum = sum(nums)
        exp_val = n * (n + 1) // 2

        return exp_val - actual_sum

       
