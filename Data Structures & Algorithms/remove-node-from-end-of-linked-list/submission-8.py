# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        slow = ListNode(-1, head)
        fast = head
        for i in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next

        if slow.val == -1:
            head = head.next
        else:
            nxt = slow.next.next
            slow.next = nxt

        return head



        