# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    memo = dict()

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        first, second = 0, 0

        self.memo[root.left] = self.rob(root.left) if root.left not in self.memo else self.memo[root.left]
        self.memo[root.right] = self.rob(root.right) if root.right not in self.memo else self.memo[root.right]
        first += self.memo[root.left] + self.memo[root.right]

        if root.left:
            self.memo[root.left.left] = self.rob(root.left.left) if root.left.left not in self.memo else self.memo[root.left.left]
            self.memo[root.left.right] = self.rob(root.left.right) if root.left.right not in self.memo else self.memo[root.left.right]
            second += self.memo[root.left.left] + self.memo[root.left.right]
        if root.right:
            self.memo[root.right.left] = self.rob(root.right.left) if root.right.left not in self.memo else self.memo[root.right.left]
            self.memo[root.right.right] = self.rob(root.right.right) if root.right.right not in self.memo else self.memo[root.right.right]
            second += self.memo[root.right.left] + self.memo[root.right.right]
        second += root.val
        return max(first, second)

    def rob2(self, root):
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        first = self.rob2(root.left) + self.rob2(root.right)
        second = root.val
        if root.left:
            second += self.rob2(root.left.left) + self.rob2(root.left.right)
        if root.right:
            second += self.rob2(root.right.left) + self.rob2(root.right.right)
        first = first if first > second else second
        self.memo[root] = first
        return first

    def rob3(self, root):
        def rob_sub(root):
            if not root:
                return 0, 0
            left = rob_sub(root.left)
            right = rob_sub(root.right)
            first = root.val + left[1] + right[1]
            second = max(left[0], left[1]) + max(right[0], right[1])
            return first, second
        rv = rob_sub(root)
        return max(rv[0], rv[1])
