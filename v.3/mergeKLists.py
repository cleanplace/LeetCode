import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next

if __name__ == "__main__":
    l1_1 = ListNode(1)
    l1_2 = ListNode(4)
    l1_3 = ListNode(5)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    l3_1 = ListNode(2)
    l3_2 = ListNode(6)
    l3_1.next = l3_2

    a = [l1_1,l2_1,l3_1]

    s = Solution()
    result =s.mergeKLists(a)

    print(result)