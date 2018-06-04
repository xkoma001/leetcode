# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        stack = [root]
        while stack:
            cur_nodes = [node for node in stack]
            pre_node = cur_nodes[0]
            for cur_node in cur_nodes[1:]:
                pre_node.next = cur_node
                pre_node = cur_node
            stack = [kid for pair in stack for kid in (pair.left, pair.right) if kid]
        return

    def connect2(self, root):
        while root and root.left:
            cur = root
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            root = root.left
        return
