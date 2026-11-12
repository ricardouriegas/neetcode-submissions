# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            tmp = head.next # look at the following node
            
            # change the direction of the current node to the prev
            head.next = prev

            prev = head # move the previous one ahead
            head = tmp # move the current one ahead

        return prev