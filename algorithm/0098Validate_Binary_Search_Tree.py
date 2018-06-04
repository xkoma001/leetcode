# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def vali_sub_bst(node):
            if not node:
                return True

            cur_min, cur_max = 0, 0
            left = vali_sub_bst(node.left)
            if left is False:
                return False
            elif left is True:
                cur_min = node.val
            else:
                cur_min = left[0]
                if node.val <= left[1]:
                    return False

            right = vali_sub_bst(node.right)
            if right is False:
                return False
            elif right is True:
                cur_max = node.val
            else:
                cur_max = right[1]
                if node.val >= right[0]:
                    return False

            return cur_min, cur_max

        return vali_sub_bst(root) is not False

    def isValidBST2(self, root):
        if not root:
            return True

        pre, stack = None, []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            if pre and pre.val >= cur.val:
                return False
            pre = cur
            root = cur.right
        return True

if __name__ == '__main__':
    s = Solution()
    from utils import make_tree
    root = make_tree([2,1,3])
    print(s.isValidBST(root))
