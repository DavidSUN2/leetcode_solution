# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# T: O(N), S: O(1)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        
        dummy = ListNode()
        dummy.next = head

        pointer_baseline = dummy
        current = head
        count = 0
        while True:
            if count < left - 1:
                pointer_baseline = pointer_baseline.next
                current = current.next

            
            if left - 1 <= count < right - 1:
                temp = pointer_baseline.next
                pointer_baseline.next = current.next
                current.next = pointer_baseline.next.next
                pointer_baseline.next.next = temp
                
                
            
            count += 1

            if count >= right - 1:
                break

        return dummy.next