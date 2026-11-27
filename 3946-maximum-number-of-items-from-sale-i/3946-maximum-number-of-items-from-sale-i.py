from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        # Step 1: free items count for each type
        free_count = [0] * n
        for i, (f_i, _) in enumerate(items):
            cnt = 0
            for j, (f_j, _) in enumerate(items):
                if i != j and f_j % f_i == 0:
                    cnt += 1
            free_count[i] = cnt

        # Step 2: 0/1 knapsack for first purchases
        # dp[b] = max items from first purchases with exact cost b
        NEG = -10**9
        dp = [NEG] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            price = items[i][1]
            value = 1 + free_count[i]  # first purchase gives this many items
            # iterate backwards to enforce 0/1 choice
            for b in range(budget, price - 1, -1):
                if dp[b - price] != NEG:
                    dp[b] = max(dp[b], dp[b - price] + value)

        # Step 3: add greedy extra copies of the cheapest item
        min_price = min(price for _, price in items)
        ans = 0
        for b in range(budget + 1):
            if dp[b] != NEG:
                extra = (budget - b) // min_price
                ans = max(ans, dp[b] + extra)

        return ans