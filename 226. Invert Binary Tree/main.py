def invertTree(root):
    if not root:
        return root
    self.invertTree(root.left)
    self.invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root