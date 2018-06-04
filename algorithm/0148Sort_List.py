# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        链表要求时间消耗为O(nlogn),空间为T(1)
        思路１:
        采用归并排序的方法，分而治之
        链表l,长度为n分裂为a,b.
        a为有序，b也为有序,合并后也为有序时间消耗为O(n),
        由于整个分治过程分为logn层,所以时间总消耗分为O(nlogn)
        思路2:
        非递归版本
        自底向上操作
        """
        if head is None:
            return head
        len, tail = 0, head
        while tail is not None:
            tail = tail.next
            len += 1
        return self.merge_sort(head, len)

    def merge_sort(self, l, len):
        if len <= 1:
            return l

        a, b, half = l, l, len//2
        # 链表断开
        for _ in range(half-1):
            b = b.next
        tmp = b.next
        b.next = None
        b = tmp

        a = self.merge_sort(a, half)
        b = self.merge_sort(b, len-half)

        head = a if a.val <= b.val else b
        pre_a = None
        while a and b:
            if b.val < a.val:
                # b值小于a值时,插入ａ前
                tmp = b.next
                b.next = a
                if pre_a:
                    pre_a.next = b
                pre_a = b
                b = tmp
            else:
                pre_a = a
                a = a.next
        if a is None:
            pre_a.next = b

        return head

    def sortList2(self, head):
        '''
        从底层
        :param head:
        :return:
        '''
        if not head:
            return None
        from collections import deque
        nodes = deque()
        while head:
            cur_node = head
            head = head.next
            cur_node.next = None
            nodes.append(cur_node)
        while len(nodes) > 1:
            m = nodes.popleft()
            n = nodes.popleft()
            # 以m为基准进行排序,此时m和n均为有序的链表
            rv_head = m if m.val < n.val else n
            pre = None
            while m or n:
                if n.val <= m.val:
                    tmp = n
                    n = n.next
                    tmp.next = m
                    if pre:
                        pre.next = tmp
                    pre = tmp
                else:
                    pre = m
                    m = m.next
            if not m:
                pre.next = n

            nodes.append(rv_head)
        return nodes[0]

if __name__ == '__main__':
    from utils import make_link, travel_list
    l = [1, 2]
    s = Solution()

    head = make_link(l)
    head = s.sortList(head)
    travel_list(head)
