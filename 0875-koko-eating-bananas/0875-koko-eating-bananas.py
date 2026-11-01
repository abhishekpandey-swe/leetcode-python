class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        low, high = 1, max(piles)

        while low <= high:

            mid = low + (high - low) // 2

            total_time = 0

            for x in piles:

                total_time += (x + mid - 1) // mid

            if total_time > h:
                low = mid + 1

            else:
                high = mid - 1

        return low

