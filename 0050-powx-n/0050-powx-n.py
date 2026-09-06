class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1.0
        current_product = x
        
        while n > 0:
            # If lowest bit is 1 (odd power), multiply into result
            if n % 2 == 1:
                res *= current_product
            
            # Square the base and halve the exponent
            current_product *= current_product
            n //= 2
            
        return res