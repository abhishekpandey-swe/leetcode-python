class Solution:
    def reverse(self, x: int) -> int:
        # 32-bit integer boundaries defined by the problem
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        result = 0
        
        # Work with the absolute value to avoid Python's negative modulo quirk
        num = abs(x)
        
        while num > 0:
            # 1. Pop the last digit
            digit = num % 10
            
            # 2. Push it to the result
            result = (result * 10) + digit
            
            # 3. Chop off the last digit from the original number
            num = num // 10
            
        # Restore the original sign
        if x < 0:
            result = -result
            
        # The problem requires returning 0 if we exceed 32-bit bounds
        if result < MIN_INT or result > MAX_INT:
            return 0
            
        return result