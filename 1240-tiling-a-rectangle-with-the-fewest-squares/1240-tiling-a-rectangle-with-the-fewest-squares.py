class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            n, m = m, n                     # n = height, m = width
        best = n * m
        # DP for lower bound: min squares to sum to an area
        total = n * m
        dp = [float('inf')] * (total + 1)
        dp[0] = 0
        for area in range(1, total + 1):
            s = 1
            while s * s <= area:
                dp[area] = min(dp[area], 1 + dp[area - s * s])
                s += 1

        heights = [0] * m

        def dfs(used: int):
            nonlocal best
            # Find lowest column
            min_h = float('inf')
            pos = -1
            for i in range(m):
                if heights[i] < min_h:
                    min_h = heights[i]
                    pos = i

            if min_h == n:
                best = min(best, used)
                return

            # Prune with lower bound
            remaining = total - sum(heights)
            if used + dp[remaining] >= best:
                return

            # Max square size at this position
            max_size = 1
            while (pos + max_size <= m and
                   heights[pos + max_size - 1] == min_h and
                   min_h + max_size <= n):
                max_size += 1
            max_size -= 1

            # Try largest first
            for s in range(max_size, 0, -1):
                for i in range(pos, pos + s):
                    heights[i] += s
                dfs(used + 1)
                for i in range(pos, pos + s):
                    heights[i] -= s

        dfs(0)
        return best