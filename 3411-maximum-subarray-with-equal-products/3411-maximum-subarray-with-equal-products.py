from math import gcd
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                prod = 1
                g = 0
                l = 1

                for k in range(i, j + 1):
                    x = nums[k]
                    prod *= x
                    g = gcd(g, x)
                    l = l // gcd(l, x) * x

                if prod == l * g:
                    ans = max(ans, j - i + 1)

        return ans