from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        # dp[c] = best score ending at column c in the previous row
        dp = points[0][:]

        for r in range(1, m):
            cur = [0] * n

            # Left-to-right pass:
            # previous column c' <= current column c
            best = -10**18
            for c in range(n):
                best = max(best, dp[c] + c)
                cur[c] = best + points[r][c] - c

            # Right-to-left pass:
            # previous column c' >= current column c
            best = -10**18
            for c in range(n - 1, -1, -1):
                best = max(best, dp[c] - c)
                cur[c] = max(cur[c], best + points[r][c] + c)

            dp = cur

        return max(dp)