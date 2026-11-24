# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
    
        while curr:
            end_adj = curr
            end = curr
            if curr.next and curr.next.next:
                while end_adj.next and end_adj.next.next:
                    end_adj = end_adj.next
                    end = end_adj.next
                end.next = curr.next
                curr.next = end
                end_adj.next = None
                if curr.next and curr.next.next:
                    curr = curr.next.next
                else:
                    return
            else:
                return
