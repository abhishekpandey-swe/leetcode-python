class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Two pointers on sorted array. O(n) time, O(1) space.
        Returns 1-based [left, right] indices summing to target.
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            two_pointer_sum = numbers[left] + numbers[right]

            if two_pointer_sum == target:
                return [left + 1, right + 1]
            elif two_pointer_sum < target:
                left += 1   # sum too small, increase it
            else:
                right -= 1  # sum too large, decrease it