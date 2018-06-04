# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        pre = dummy = ListNode(0)
        new_lists = [cur for cur in lists if cur]
        sort_lists = sorted(new_lists, key=lambda x: x.val)

        while sort_lists:
            small = sort_lists.pop(0)
            pre.next = small
            pre = small
            if small.next:
                cur_node = small.next
                i, m_len =0, len(sort_lists)
                while i < m_len:
                    if cur_node.val < sort_lists[i].val:
                        sort_lists.insert(i, cur_node)
                        break
                    i += 1
                if i == m_len:
                    sort_lists.append(cur_node)
        return dummy.next

    def mergeKLists2(self, lists):
        import heapq
        p_queue = []
        for node in lists:
            if node:
                heapq.heappush(p_queue, [node.val, node])

        tail = dummy = ListNode(0)
        while p_queue:
            pair = heapq.heappop(p_queue)
            tail.next = pair[1]
            tail = pair[1]
            if tail.next:
                heapq.heappush([tail.next.val, tail.next])
        return dummy.next


