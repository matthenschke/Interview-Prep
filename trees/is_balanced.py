# https://leetcode.com/problems/balanced-binary-tree/submissions/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


def getHeight(root):
    if not root:
        return 0
    return 1 + max(getHeight(root.right), getHeight(root.left))
