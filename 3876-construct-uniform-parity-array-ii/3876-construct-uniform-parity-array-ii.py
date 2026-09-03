class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        # Step 1: Initialize boundaries to infinity
        min_odd = float('inf')
        min_even = float('inf')
        
        # Step 2: Track the smallest odd and smallest even numbers in one pass
        for num in nums:
            if num % 2 == 0:
                if num < min_even:
                    min_even = num
            else:
                if num < min_odd:
                    min_odd = num
                    
        # Step 3: Evaluate our two core insights
        
        # If the array is already perfectly uniform (all odds or all evens)
        if min_odd == float('inf') or min_even == float('inf'):
            return True
            
        # To make everything odd, the smallest even MUST be larger than the smallest odd
        return min_even > min_odd