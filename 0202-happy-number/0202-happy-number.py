class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)

        while fast != 1 and slow != fast:
            slow = self.sumOfSquares(slow)              # 1 step
            fast = self.sumOfSquares(self.sumOfSquares(fast))  # 2 steps

        return fast == 1

    def sumOfSquares(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total