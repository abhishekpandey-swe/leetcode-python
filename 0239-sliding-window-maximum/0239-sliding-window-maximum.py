from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Return the maximum value of every contiguous window of size k."""
        
        dq = deque()
        result = []

        for right in range(len(nums)):
            while dq and dq[-1][0] < nums[right]:
                dq.pop()

            dq.append((nums[right], right))

            while dq and dq[0][1] <= right - k:
                dq.popleft()

            if right >= k - 1:
                result.append(dq[0][0])

        return result