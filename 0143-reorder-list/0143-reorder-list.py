# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # ---------- Step 1: Find middle (slow/fast) ----------
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle node of the first half

        # ---------- Step 2: Reverse second half ----------
        prev, cur = None, slow.next
        slow.next = None               # cut the list into two halves
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # `prev` is the head of the reversed second half

        # ---------- Step 3: Merge two halves alternately ----------
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2