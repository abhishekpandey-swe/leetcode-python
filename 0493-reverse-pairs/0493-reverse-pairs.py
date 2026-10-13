from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0] * n

        def merge_sort(left: int, right: int) -> int:
            if right - left <= 1:
                return 0

            mid = (left + right) // 2

            count = merge_sort(left, mid) + merge_sort(mid, right)

            # Count cross reverse pairs:
            # nums[i] > 2 * nums[j], where i in left half, j in right half
            j = mid
            for i in range(left, mid):
                while j < right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid

            # Merge two sorted halves into temp
            i, j, k = left, mid, left

            while i < mid and j < right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            while i < mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j < right:
                temp[k] = nums[j]
                j += 1
                k += 1

            # Copy back from temp to nums
            for k in range(left, right):
                nums[k] = temp[k]

            return count

        return merge_sort(0, n)