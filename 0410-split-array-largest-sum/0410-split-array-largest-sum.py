class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        def can_split(max_sum : int) -> bool:

            subarrays = 1
            curr_sum = 0

            for num in nums:

                if curr_sum + num <= max_sum:
                    curr_sum += num

                else:
                    subarrays += 1
                    curr_sum = num

                    if subarrays > k:
                        return False


            return True

        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = low + (high - low) // 2

            if can_split(mid):
                high = mid

            else:
                low = mid + 1

        return low


