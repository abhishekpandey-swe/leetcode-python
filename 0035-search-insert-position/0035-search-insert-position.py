class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        n = len(nums)
        low, high = 0, n - 1
        ans = n

        while low <= high:
            mid = low + (high - low) // 2

            # Maybe we can find ans

            if nums[mid] >= target:
                ans = mid

                # Look for smaller idx in left
                high = mid - 1

            else:
                # Look for higher idx in right
                low = mid + 1

        return ans
