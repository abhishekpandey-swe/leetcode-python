import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # max-heap via negation → lower half
        self.large = []   # min-heap              → upper half

    def addNum(self, num: int) -> None:
        # 1. Push to max-heap (lower half)
        heapq.heappush(self.small, -num)

        # 2. Move the largest of `small` into `large`
        #    → guarantees every element of `small` <= every element of `large`
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # 3. Rebalance size: keep len(small) >= len(large)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])                 # odd count
        return (-self.small[0] + self.large[0]) / 2.0    # even count