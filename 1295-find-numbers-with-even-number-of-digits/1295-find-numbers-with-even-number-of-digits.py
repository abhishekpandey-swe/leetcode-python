class Solution:
    def findNumbers(self, nums: list[int]) -> int:

        length = 0

        for num in nums:
           digit = len(str(num))

           if digit % 2 == 0:
              length += 1

        return length