from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        # Count occurrences of each factor
        cnt_factor = [0] * (n + 1)
        min_price = float('inf')
        for factor, price in items:
            cnt_factor[factor] += 1
            min_price = min(min_price, price)

        # Precompute the number of multiples for each factor
        cnt_multi = [0] * (n + 1)
        # Group double-slots by price: price -> total number of slots
        # (Only consider items with price < 2 * min_price)
        from collections import defaultdict
        slots_by_price = defaultdict(int)

        for factor, price in items:
            if price >= 2 * min_price:
                continue
            if cnt_multi[factor] == 0:
                # Harmonic-series sieve
                for mult in range(factor, n + 1, factor):
                    cnt_multi[factor] += cnt_factor[mult]
            # Number of free items this factor can generate
            free_cnt = cnt_multi[factor] - 1  # exclude itself
            if free_cnt > 0:
                slots_by_price[price] += free_cnt

        ans = 0
        # Greedily take double-slots from cheapest to most expensive
        for price in sorted(slots_by_price):
            if budget < price:
                break
            cnt = slots_by_price[price]
            can_buy = min(cnt, budget // price)
            ans += 2 * can_buy
            budget -= can_buy * price

        # Spend the rest on the cheapest single item
        ans += budget // min_price
        return ans