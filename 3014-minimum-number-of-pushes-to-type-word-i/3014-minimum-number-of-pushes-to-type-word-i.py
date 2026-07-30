class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        
        # Iterate through each character by its index (0 to n-1)
        for i in range(n):
            # i // 8 tells us which "layer" of the keypad we are on.
            # Layer 0 (front): cost 1
            # Layer 1 (behind): cost 2
            # Layer 2 (third): cost 3
            cost = (i // 8) + 1
            total_pushes += cost
            
        return total_pushes