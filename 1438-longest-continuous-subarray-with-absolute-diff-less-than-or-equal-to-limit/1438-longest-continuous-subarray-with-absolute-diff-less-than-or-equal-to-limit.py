from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxDeque = deque()
        minDeque = deque()

        left = 0
        max_length = 0

        for right in range(len(nums)):

            # MAX → decreasing
            while maxDeque and maxDeque[-1][0] < nums[right]:
                maxDeque.pop()

            maxDeque.append((nums[right], right))

            # MIN → increasing
            while minDeque and minDeque[-1][0] > nums[right]:
                minDeque.pop()

            minDeque.append((nums[right], right))

            # Shrink while window is invalid
            while maxDeque[0][0] - minDeque[0][0] > limit:

                if maxDeque[0][1] == left:
                    maxDeque.popleft()

                if minDeque[0][1] == left:
                    minDeque.popleft()

                left += 1

            # Current window is valid
            max_length = max(max_length, right - left + 1)

        return max_length