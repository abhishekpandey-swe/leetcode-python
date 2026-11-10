class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = low + (high - low) // 2

            subarrays = 1
            curr_sum = 0

            for num in nums:
                    
                if curr_sum + num > mid:
                    subarrays += 1
                    curr_sum = num 

                else:
                    curr_sum += num

            if subarrays <= k:
                high = mid

            else:
                low = mid + 1

        return low



