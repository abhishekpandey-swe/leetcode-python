class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
        
        # Helper to generate a palindrome from a left half
        def make_palindrome(left: int, is_even: bool) -> int:
            res = left
            # If odd length, skip the last digit when mirroring
            if not is_even:
                left //= 10
            while left > 0:
                res = res * 10 + left % 10
                left //= 10
            return res
        
        # Extract the first half (including middle for odd length)
        left_half = int(n[:(length + 1) // 2])
        is_even = (length % 2 == 0)
        
        # Generate the 5 candidates
        candidates = set()
        candidates.add(make_palindrome(left_half, is_even))
        candidates.add(make_palindrome(left_half - 1, is_even))
        candidates.add(make_palindrome(left_half + 1, is_even))
        candidates.add(10**(length - 1) - 1)  # e.g., 999
        candidates.add(10**length + 1)        # e.g., 1001
        
        # Find the closest one, excluding the original number
        best = None
        min_diff = float('inf')
        
        for cand in candidates:
            if cand == num:
                continue
            diff = abs(cand - num)
            # If diff is smaller, or diff is tie but candidate is smaller
            if diff < min_diff or (diff == min_diff and cand < best):
                min_diff = diff
                best = cand
                
        return str(best)