# https://leetcode.com/problems/n-ary-tree-preorder-traversal/


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node'):

        def preorder_hlp(root, arr):
            if root:
                arr.append(root.val)
                for child in root.children:
                    preorder_hlp(child, arr)

        arr = []
        if not root:
            return arr

        preorder_hlp(root, arr)
        return arr
