from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Step 1: Precompute suffix sums to get remaining stones in O(1) time
        # suffix[i] represents the total stones from index i to the end.
        suffix = [0] * n
        suffix[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
            
        # Step 2: Define our DP function with memoization
        @lru_cache(None)
        def dp(i, m):
            # Base Case: If we can take all remaining piles, we take them all.
            if i + 2 * m >= n:
                return suffix[i]
            
            # Step 3: Try all possible moves (taking 1 to 2*m piles)
            # We want to MINIMIZE the opponent's future score.
            min_opponent_score = float('inf')
            
            for x in range(1, 2 * m + 1):
                # Opponent's best score if we take 'x' piles
                opponent_score = dp(i + x, max(m, x))
                min_opponent_score = min(min_opponent_score, opponent_score)
                
            # Our max score is the total available minus the opponent's best possible score
            return suffix[i] - min_opponent_score
            
        # Alice starts at index 0 with M = 1
        return dp(0, 1)