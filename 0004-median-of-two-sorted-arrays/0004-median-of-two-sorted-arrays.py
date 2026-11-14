class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half = (m + n + 1) // 2  # size of left half

        while low <= high:
            i = (low + high) // 2          # cut in nums1
            j = half - i                   # cut in nums2

            maxLeft1  = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf')  if i == m else nums1[i]
            maxLeft2  = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf')  if j == n else nums2[j]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Valid partition
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    return float(max(maxLeft1, maxLeft2))
            elif maxLeft1 > minRight2:
                high = i - 1   # move cut left in nums1
            else:
                low = i + 1    # move cut right in nums1

        raise ValueError("Input arrays are not sorted")