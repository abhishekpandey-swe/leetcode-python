class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # rec = [x1, y1, x2, y2]
        
        # 1. Check overlap on the X-axis (Horizontal)
        # The left-most right edge must be greater than the right-most left edge.
        x_overlap = min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])
        
        # 2. Check overlap on the Y-axis (Vertical)
        # The bottom-most top edge must be greater than the top-most bottom edge.
        y_overlap = min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])
        
        # They only overlap in 2D space if they overlap on both axes
        return x_overlap and y_overlap