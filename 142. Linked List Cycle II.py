# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# T: O(N), S: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while not(fast is None or fast.next is None or fast.next.next is None):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while True:
                    if slow == fast:
                        return slow
                    slow = slow.next
                    fast = fast.next
        return None