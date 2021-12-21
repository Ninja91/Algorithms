class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class PostOrderIterator:
    def __init__(self, root: 'TreeNode'):
        self.stack = []
        self.initialize(root)

    def initialize(self, root: 'TreeNode'):
        if root:
            self.stack.append(root)
            if root.left:
                self.initialize(root.left)
            else:
                self.initialize(root.right)

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        next_ele = self.stack.pop()
        if self.stack and next_ele == self.stack[-1].left:
            parent = self.stack[-1]  # type: 'TreeNode'
            self.initialize(parent.right)
        return next_ele.val
