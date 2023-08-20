"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# T: O(N), S: O(1)
class Solution:
    def flatten(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            if curr.child is not None:
                tmp = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                curr_child = curr.child
                while curr_child.next:
                    curr_child = curr_child.next
                curr_child.next = tmp
                if tmp is not None:
                    tmp.prev = curr_child
                curr.child = None
            
            curr = curr.next
        return head