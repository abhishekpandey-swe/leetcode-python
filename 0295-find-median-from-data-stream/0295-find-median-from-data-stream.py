import bisect

class MedianFinder:

    def __init__(self):
        self.nums = []                  # maintained in sorted order

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)   # O(n) shift, O(log n) search

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return float(self.nums[n // 2])
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0