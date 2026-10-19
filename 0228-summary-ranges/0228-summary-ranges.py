class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
            
        result = []
        start = 0 # Our "finger" marking the start of a range
        
        for i in range(len(nums)):
            # If we are at the end OR the sequence breaks
            if i == len(nums) - 1 or nums[i] + 1 != nums[i+1]:
                
                # Check if the range is just one number (start and i are the same)
                if start == i:
                    result.append(str(nums[start]))
                # Otherwise, it's a multi-number range
                else:
                    result.append(f"{nums[start]}->{nums[i]}")
                
                # Move the start pointer to the next number for the next range
                start = i + 1
                
        return result