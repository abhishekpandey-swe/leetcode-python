class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        ans = nums[0]
        max_product = nums[0]
        min_product = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            
            curr_max = max(x , max_product * x , min_product * x)
            curr_min = min(x , max_product * x , min_product * x)

            max_product = curr_max
            min_product = curr_min 

            ans = max(ans , max_product)

        return ans


        