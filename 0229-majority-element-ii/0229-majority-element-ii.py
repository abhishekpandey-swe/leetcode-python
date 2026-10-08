class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # --- Phase 1: Find the two candidates ---
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # --- Phase 2: Single-pass verification ---
        res = []
        count1, count2 = 0, 0  # Reset counters for the verification pass
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
                
        # Check candidate 1
        if cand1 is not None and count1 > n // 3:
            res.append(cand1)
            
        # Check candidate 2
        if cand2 is not None and count2 > n // 3:
            res.append(cand2)

        return res



