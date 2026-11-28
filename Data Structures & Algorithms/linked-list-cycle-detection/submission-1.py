# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # bag = set()

        # while head:
        #     if head not in bag:
        #         bag.add(head)
        #     else:
        #         return True
            
        #     head = head.next

        # return False

        fast = head

        while fast and fast.next:
            # head will be going 1 by 1
            head = head.next
            fast = fast.next.next

            if fast == head:
                return True

        return False
