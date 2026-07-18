class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Return the total amount of trapped rain water.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """

        if not height:
            return 0

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        total_water = 0

        while left < right:

            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                total_water += left_max - height[left]
                left += 1
            else:
                total_water += right_max - height[right]
                right -= 1

        return total_water