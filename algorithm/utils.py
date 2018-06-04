# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_tree(l):
    if not l:
        return None
    root = TreeNode(l[0])
    l.pop(0)
    stack = [root]
    while stack and l:
        cur = stack.pop(0)
        if l[0] is None:
            cur.left = None
        else:
            cur.left = TreeNode(l[0])
            stack.append(cur.left)
        l.pop(0)
        if l:
            if l[0] is None:
                cur.right = None
            else:
                cur.right = TreeNode(l[0])
                stack.append(cur.right)
            l.pop(0)
    return root


def make_link(l):
    if not l:
        return None

    head = ListNode(l[0])
    cur_node = head
    for val in l[1:]:
        new_node = ListNode(val)
        cur_node.next = new_node
        cur_node = new_node

    return head


def travel_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

if __name__ == "__main__":
    l = [3, 5, 8, 9, 12, 6]
    link_list = make_link(l)
    travel_list(link_list)
