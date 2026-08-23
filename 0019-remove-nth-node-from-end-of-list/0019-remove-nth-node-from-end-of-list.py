# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Initialize a dummy node to cleanly handle edge cases
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # 2. Advance the right pointer (scout) by n steps
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # 3. Move both pointers until right reaches the end of the list
        while right:
            left = left.next
            right = right.next
            
        # 4. left is now just before the node we want to delete. Skip it.
        left.next = left.next.next
        
        # Return the actual head of the list (bypassing the dummy)
        return dummy.next
        