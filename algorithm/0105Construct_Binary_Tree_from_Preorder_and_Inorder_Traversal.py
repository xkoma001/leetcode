# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        in_offset = inorder.index(root_val)
        l_in = inorder[:in_offset]
        r_in = inorder[in_offset+1:]
        l_len = len(l_in)
        l_pre = preorder[1:1+l_len]
        r_pre = preorder[1+l_len:]

        root.left = self.buildTree(l_pre, l_in)
        root.right = self.buildTree(r_pre, r_in)
        return root

if __name__ == '__main__':
    s = Solution()
    print(s.buildTree([1,2,3], [3,2,1]))
