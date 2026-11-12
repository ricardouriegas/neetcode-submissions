# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            tmp = cur.next # look at the following node
            
            # change the direction of the current node to the prev
            cur.next = prev

            prev = cur # move the previous one ahead
            cur = tmp # move the current one ahead

        return prev