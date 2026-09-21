class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
        counts = collections.Counter(nums1)
        res = []
        for n in nums2:
            if counts[n] > 0:
                res.append(n)
                counts[n] -= 1
        return res