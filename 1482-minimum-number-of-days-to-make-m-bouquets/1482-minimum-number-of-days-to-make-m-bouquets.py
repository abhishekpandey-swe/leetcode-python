class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        low, high = 1, max(bloomDay)

        while low < high:

            mid = low + (high - low) // 2

            bouquets = 0
            consecutive = 0

            for flower in bloomDay:
                if flower <= mid:
                    consecutive += 1


                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0

                        if bouquets > m:
                            break

                else:

                    consecutive = 0

            if bouquets >= m:
                high = mid

            else:
                low = mid + 1

        return low







        