import heapq

# https://leetcode.com/problems/merge-k-sorted-lists/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

        if not lists:
            return None
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, lists[i])
        head, tail = None, None
        while heap:
            temp = heapq.heappop(heap)
            if temp.next:
                heapq.heappush(heap, temp.next)

            if not head:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head
