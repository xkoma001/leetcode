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
        if not root:
            return

        next_level = root
        while next_level:
            cur = next_level
            pre, next_level = None, None
            while cur:
                if cur.left:
                    if not pre:
                        pre = cur.left
                        next_level = pre
                    else:
                        pre.next = cur.left
                        pre = cur.left
                if cur.right:
                    if not pre:
                        pre = cur.right
                        next_level = pre
                    else:
                        pre.next = cur.right
                        pre = cur.right
                cur = cur.next
        return

if __name__ == '__main__':
    s = Solution()
    node = TreeLinkNode(0)
    print(s.connect2(node))
