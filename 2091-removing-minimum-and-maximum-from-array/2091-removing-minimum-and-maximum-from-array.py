class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        a = nums.index(min(nums))
        b = nums.index(max(nums))
        if a > b:
            a, b = b, a
        return min(b+1, n-a, (a+1)+(n-b))