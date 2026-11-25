# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        ptr = head
        cnt = 0
        while ptr:
            cnt += 1
            ptr = ptr.next

        idx = cnt - n
        if idx == 0:
            return head.next
        slow = head
        fast = head.next.next
        for i in range(idx - 1):
            slow = slow.next
            fast = fast.next
        slow.next = fast
        return head

        