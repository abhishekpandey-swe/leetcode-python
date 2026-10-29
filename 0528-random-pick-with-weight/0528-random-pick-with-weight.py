from typing import List
import random
import bisect

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = [0]
        for weight in w:
            self.prefix.append(self.prefix[-1] + weight)

        self.total = self.prefix[-1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        idx = bisect.bisect_left(self.prefix, target)
        return idx - 1
        