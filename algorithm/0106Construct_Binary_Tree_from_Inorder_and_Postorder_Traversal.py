# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)
        ind = inorder.index(root_val)
        l_len = len(inorder[:ind])
        root.left = self.buildTree(inorder[:ind], postorder[:l_len])
        root.right = self.buildTree(inorder[ind+1:], postorder[l_len:])
        return root
