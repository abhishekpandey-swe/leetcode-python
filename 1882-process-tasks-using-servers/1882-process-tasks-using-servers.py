import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Idle heap: (weight, index)
        idle = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(idle)
        
        # Busy heap: (finish_time, weight, index)
        busy = []
        res = []
        current_time = 0
        
        for i, task_duration in enumerate(tasks):
            current_time = max(current_time, i)
            
            # Move finished servers from busy to idle
            while busy and busy[0][0] <= current_time:
                finish, w, idx = heapq.heappop(busy)
                heapq.heappush(idle, (w, idx))
            
            # If no idle server, wait until the earliest one finishes
            if not idle:
                current_time = busy[0][0]
                while busy and busy[0][0] <= current_time:
                    finish, w, idx = heapq.heappop(busy)
                    heapq.heappush(idle, (w, idx))
            
            # Assign task to the best available server
            w, idx = heapq.heappop(idle)
            res.append(idx)
            heapq.heappush(busy, (current_time + task_duration, w, idx))
            
        return res