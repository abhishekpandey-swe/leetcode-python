from math import gcd
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 2          # Any two numbers always work
        left = 0
        prod = 1         # Product of the current window

        for right, x in enumerate(nums):
            # Shrink until x is coprime with every element in the window
            while gcd(prod, x) > 1:
                prod //= nums[left]
                left += 1

            prod *= x
            ans = max(ans, right - left + 1)

        return ans