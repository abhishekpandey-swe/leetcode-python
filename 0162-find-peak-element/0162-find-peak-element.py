class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] < nums[mid + 1]:
                # Going up; peak must be to the right
                lo = mid + 1
            else:
                # Going down; peak must be on the left, including mid
                hi = mid

        return lo