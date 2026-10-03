class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x
        
        low, high = 1, x // 2
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            sq = mid * mid
            
            if sq == x:
                return mid
            elif sq < x:
                ans = mid       # mid is a candidate
                low = mid + 1   # try to find a bigger one
            else:
                high = mid - 1  # mid too big
        
        return ans

        