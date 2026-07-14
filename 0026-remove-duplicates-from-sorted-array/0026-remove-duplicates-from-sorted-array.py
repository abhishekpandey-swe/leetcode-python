class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0

        # i: write pointer
        i = 1

        # j: read pointer
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return i
