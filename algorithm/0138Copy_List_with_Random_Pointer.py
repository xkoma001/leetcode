# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        cur_node = None
        old, new = {}, []

        count = 0
        old_node = head
        while head:
            old[head] = count
            if not cur_node:
                cur_node = RandomListNode(head.label)
            else:
                cur_node.next = RandomListNode(head.label)
                cur_node = cur_node.next
            new.append(cur_node)
            head = head.next
            count += 1

        head = old_node
        count = 0
        while head:
            if head.random:
                new[count].random = new[old[head.random]]
            else:
                new[count].random = None
            head = head.next
            count += 1
        return new[0]

    def copyRandomList2(self, head):
        if not head:
            return head

        cur = head
        while cur:
            second = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = second
            cur = second

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        new_head = head.next
        cur = head
        new_pre = None
        while cur:
            new = cur.next
            cur.next = cur.next.next

            if new_pre:
                new_pre.next = new
            new_pre = new
            cur = cur.next
        return new_head
