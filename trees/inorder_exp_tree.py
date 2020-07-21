class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isOperator(ch):
    if ch == "+" or ch == "-" or ch == "*" or ch == "/":
        return True
    return False


def constructTree(exp):
    if not exp:
        return
    stack = []
    for ch in exp:
        node = TreeNode(ch)
        if isOperator(ch):
            t1 = stack.pop()
            t2 = stack.pop()
            node.left = t2
            node.right = t1

        stack.append(node)

    return stack.pop()


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)
