class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_count = {0 : 1}
        prefix_sum = 0
        count= 0

        for num in nums:
            prefix_sum += num

            count += prefix_count.get(prefix_sum-k, 0)

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count