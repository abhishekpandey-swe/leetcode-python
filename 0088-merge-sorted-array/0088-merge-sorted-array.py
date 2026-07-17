class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Time Complexity:
            O(m + n)

        Space Complexity:
            O(1)
        """
        # Pointer to the last valid element in nums1
        i = m -1 
        # Pointer to the last valid element in nums2
        j = n - 1
        # Pointer to the last position of nums1
        write = m + n - 1

        while i >= 0 and j >= 0 :
            if nums1[i] > nums2[j] :
                nums1[write] = nums1[i]
                i -= 1

            else :
                nums1[write] = nums2[j]
                j -= 1
            write -= 1

        while j >= 0 :
            nums1[write] = nums2[j]
            j -= 1
            write -= 1
        