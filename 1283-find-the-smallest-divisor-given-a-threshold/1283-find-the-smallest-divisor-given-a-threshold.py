class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:

        low, high = 1, max(nums)

        while low < high:
            mid = low + (high - low) // 2

            total = 0 

            for num in nums:

                total += (num + mid - 1) // mid

            if total > threshold:
                low = mid + 1

            else:
                high = mid

        return low