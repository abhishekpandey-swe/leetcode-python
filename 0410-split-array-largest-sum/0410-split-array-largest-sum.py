from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2
            if self._can_split(nums, k, mid):
                high = mid          # mid feasible → try smaller
            else:
                low = mid + 1       # mid too small → need larger

        return low

    def _can_split(self, nums: List[int], k: int, limit: int) -> bool:
        count, current = 1, 0
        for num in nums:
            if current + num > limit:
                count += 1
                current = num
                if count > k:
                    return False    # prune early
            else:
                current += num
        return True