class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        n = len(nums) # Added this line

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

        # Second pass: verify the candidates
        res = []
        
        # Fixed the tuple logic here
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > n // 3:
                if cand not in res:
                    res.append(cand)

        return res # Fixed variable name here