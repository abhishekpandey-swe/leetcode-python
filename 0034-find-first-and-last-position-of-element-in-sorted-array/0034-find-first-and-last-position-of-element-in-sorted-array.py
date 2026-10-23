import bisect 

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        # bisect_left is exactly lower_bound

        start = bisect.bisect_left(nums, target)

        # Check if target exists
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        # bisect_right is exactly upper_bound

        end = bisect.bisect_right(nums, target) - 1

        return [start, end]





        