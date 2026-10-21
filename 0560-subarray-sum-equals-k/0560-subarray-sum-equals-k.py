from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1  # empty prefix

        for num in nums:
            prefix += num

            # number of previous prefixes that make sum k
            count += seen[prefix - k]

            seen[prefix] += 1

        return count