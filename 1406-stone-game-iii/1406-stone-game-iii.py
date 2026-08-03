class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        
        # dp[i] will store the max score difference the current player 
        # can get from index i to the end.
        dp = [0] * (n + 1)
        
        # Work backwards from the end of the array
        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            take = 0
            
            # We can take 1, 2, or 3 stones 
            for k in range(1, 4):
                # Ensure we don't go out of bounds of the stone array
                if i + k - 1 < n:
                    take += stoneValue[i + k - 1]
                    
                    # Score difference = stones taken MINUS opponent's optimal future score
                    dp[i] = max(dp[i], take - dp[i + k])
                    
        # Evaluate Alice's final relative score against Bob
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"