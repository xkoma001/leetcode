# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        考虑各种边界条件
        思路１:
        将链表中的值，转换成整数值
        相加后，在逆序保存到链表中
        假设l1长度为m,l2长度为n则
        时间开销为O(max(m,n))
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        思路2:
        直接在链表上做位操作相加,按照整数运算法则操作
        每一位的值为cur_val = (x+y+carry)%/10
        进位制为 carry = (x+y+carry)/10
        时间开销为O(max(m,n))
        """
        r1, r2, base = 0, 0, 1
        while l1 or l2:
            if l1:
                r1 += base * l1.val
                l1 = l1.next
            if l2:
                r2 += base * l2.val
                l2 = l2.next
            base *= 10

        rv = r1 + r2
        if rv == 0:
            return ListNode(0)

        dummy_head = ListNode(0)
        tail = dummy_head
        while rv != 0:
            cur_val = rv % 10
            new_node = ListNode(cur_val)
            tail.next = new_node
            tail = new_node

            rv = rv // 10
        return dummy_head.next

    def addTwoNumbers2(self, l1, l2):
        dummy_head, carry= ListNode(0), 0
        tail = dummy_head
        while l1 or l2:
            r1, r2 = 0, 0
            if l1:
                r1 = l1.val
                l1 = l1.next
            if l2:
                r2 = l2.val
                l2 = l2.next

            sum = r1 + r2 + carry
            carry = sum // 10
            tail.next = ListNode(sum % 10)
            tail = tail.next

        if carry == 1:
            tail.next = ListNode(1)
        return dummy_head.next

if __name__ == '__main__':
    from utils import make_link, travel_list
    s = Solution()
    l1, l2 = [9, 8], [1]
    l1 = make_link(l1)
    l2 = make_link(l2)
    head = s.addTwoNumbers2(l1, l2)
    travel_list(head)

