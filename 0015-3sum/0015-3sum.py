class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Find all unique triplets that sum to zero.

        Approach: Sort + Two Pointers
        Time Complexity:  O(n^2)
        Space Complexity: O(1) excluding output
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):

            # Skip duplicates for the pivot element.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            L, R = i + 1, n - 1

            while L < R:
                current_sum = nums[L] + nums[R]

                if current_sum == target:
                    result.append([nums[i], nums[L], nums[R]])

                    # Skip duplicates for L.
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1

                    # Skip duplicates for R.
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1

                    L += 1
                    R -= 1

                elif current_sum > target:
                    R -= 1

                else:
                    L += 1

        return result