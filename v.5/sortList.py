class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge(a, b):

            if not a:
                return b

            elif not b:
                return a

            if a.val < b.val:
                a.next = merge(a.next, b)
                return a

            else:
                b.next = merge(a, b.next)
                return b


        if head is None:
            return None

        elif head.next is None:
            return head


        pre, slow, fast = None, head, head

        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None

        # sort by divide-and-conquer

        first_half = self.sortList(head)
        second_half = self.sortList(slow)
        result = merge(first_half, second_half)
        return result
