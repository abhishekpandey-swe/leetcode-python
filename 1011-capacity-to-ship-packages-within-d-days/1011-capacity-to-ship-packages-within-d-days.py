class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        # Helper function to check if a given capacity is enough

        def canShip(capacity: int) -> bool:

            current_load = 0
            days_needed = 1

            for w in weights:         # w stand for weight 

                if current_load + w > capacity:
                    days_needed += 1
                    current_load = w

                else:
                    current_load += w

            return days_needed <= days

        low = max(weights)
        high = sum(weights)

        while low < high:

            mid = low + (high - low) // 2

            if canShip(mid):
                high = mid 

            else:
                low = mid + 1

        return low
