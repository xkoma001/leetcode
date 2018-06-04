# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        first, second, pre = None, None, None

        def travel_tree(node):
            nonlocal first
            nonlocal second
            nonlocal pre
            if not node:
                return None

            travel_tree(node.left)
            if pre and not first and node.val <= pre.val:
                first = pre
            if pre and first and node.val <= pre.val:
                second = node
            pre = node
            travel_tree(node.right)
            return

        travel_tree(root)
        if first and second:
            first.val, second.val = second.val, first.val
        return

    def recoverTree2(self, root):
        pre, first, second = None, None, None
        cur = root
        while cur:
            if not cur.left:
                if pre and not first and cur.val <= pre.val:
                    first = pre
                if pre and first and cur.val <= pre.val:
                    second = cur
                pre = cur
                cur = cur.right
            else:
                after = cur.left
                while after.right and after.right != cur:
                    after = after.right

                if not after.right:
                    after.right = cur
                    cur = cur.left
                else:
                    after.right = None
                    if pre and not first and cur.val <= pre.val:
                        first = pre
                    if pre and first and cur.val <= pre.val:
                        second = cur
                    pre = cur
                    cur = cur.right

        if first and second:
            first.val, second.val = second.val, first.val
        return

if __name__ == '__main__':
    s = Solution()
    print(s.recoverTree2(None))
