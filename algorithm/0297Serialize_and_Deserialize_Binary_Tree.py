# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import pickle


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        from collections import deque
        queue = deque([root])

        while len(queue) > 0:
            item = queue.popleft()
            if item is not None:
                ans.append(item.val)
                queue.append(item.left)
                queue.append(item.right)
            else:
                ans.append(None)
        return pickle.dumps(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        ans = pickle.loads(data)
        from collections import deque
        queue = deque([])
        val = ans.pop(0)
        if val is None:
            return None
        root = TreeNode(val)
        queue.append(root)

        while len(queue) > 0:
            left = ans.pop(0)
            right = ans.pop(0)
            node = queue.popleft()
            left_node, right_node = None, None
            if left is not None:
                left_node = TreeNode(left)
                queue.append(left_node)
            if right is not None:
                right_node = TreeNode(right)
                queue.append(right_node)
            node.left, node.right = left_node, right_node
        return root

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []

        def do_it(node):
            if node is None:
                ans.append('#')
                return None
            ans.append(str(node.val))
            do_it(node.left)
            do_it(node.right)
        do_it(root)
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def do_it():
            cur_val = next(vals)
            if cur_val == '#':
                return None
            node = TreeNode(int(cur_val))
            node.left = do_it()
            node.right = do_it()
            return node
        vals = iter(data.split(','))
        return do_it()

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))