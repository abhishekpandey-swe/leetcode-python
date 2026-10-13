from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2
            left, cnt_left = merge_sort(arr[:mid])
            right, cnt_right = merge_sort(arr[mid:])
            
            cnt = cnt_left + cnt_right
            
            # Count reverse pairs between left and right
            i = 0
            for y in right:
                while i < len(left) and left[i] <= 2 * y:
                    i += 1
                cnt += len(left) - i
            
            # Merge two sorted halves
            merged = []
            p = q = 0
            while p < len(left) and q < len(right):
                if left[p] <= right[q]:
                    merged.append(left[p])
                    p += 1
                else:
                    merged.append(right[q])
                    q += 1
            
            merged.extend(left[p:])
            merged.extend(right[q:])
            
            return merged, cnt
        
        return merge_sort(nums)[1]