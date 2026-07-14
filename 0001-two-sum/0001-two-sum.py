from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach : HashMap - store complement lookup.
        Time Complexity : O(n)
        Space Complexity : O(n)
        """
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
