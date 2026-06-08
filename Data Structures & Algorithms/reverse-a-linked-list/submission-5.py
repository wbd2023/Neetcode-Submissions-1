# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single-node list is already reversed.
        if head is None or head.next is None:
            return head

        # Reverse everything after head.
        new_head = self.reverseList(head.next)

        # Put head after its next node.
        head.next.next = head

        # Break the old forward link.
        head.next = None

        # The new head stays the same all the way back up.
        return new_head
