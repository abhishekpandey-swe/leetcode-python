class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        freq = {}

        # Step 1: Count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Check against the threshold
        res = []
        for num, count in freq.items():
            if count > n // 3:
                res.append(num)

        return res