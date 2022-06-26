# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        # now length = 2+

        pointer1 = head
        pointer2 = head
        pointer_lag = head
        pointer_lag2 = None

        while pointer2 is not None and pointer2.next is not None:
            pointer2 = pointer2.next.next
            pointer_lag = pointer1
            pointer1 = pointer1.next
            pointer_lag.next = pointer_lag2
            pointer_lag2 = pointer_lag

        if pointer2 is None:
            pointer2 = pointer1
            pointer1 = pointer_lag
        else:

            pointer2 = pointer1.next
            pointer1 = pointer_lag

        while pointer1 is not None and pointer2 is not None:
            if pointer1.val != pointer2.val:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return True
