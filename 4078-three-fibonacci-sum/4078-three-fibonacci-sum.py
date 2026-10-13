class Solution:
    def threeFibonacciSum(self, n: int) -> bool:

        # Handle edge case

        if n % 2 != 0 or n <= 0:
            return False

        target = n // 2

        # Generate Fibonacci terms

        a, b = 0, 1
        while b <= target:
            if b == target:
                return True

            a, b = b, a+b

        return False

    
        