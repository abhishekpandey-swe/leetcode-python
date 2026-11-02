class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        def canMakeBouquets(day: int) -> bool:
            bouquets = 0
            consecutive = 0

            for flower in bloomDay:
                if flower <= day:
                    consecutive += 1

                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0

                        if bouquets >= m:
                            return True 

                else:
                    consecutive = 0

            return False

        # Binary search on answer

        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = low + (high - low) // 2

            if canMakeBouquets(mid):
                high = mid - 1

            else:
                low = mid + 1

        return low
