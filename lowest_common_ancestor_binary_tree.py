class Solution:
    def lowetsCommonAncrestor(self, root, p, q):
        if root is None:
            return
        if root == q or root == p:
            return root
        left = self.lowetsCommonAncrestor(root.left, p, q)
        right = self.lowetsCommonAncrestor(root.right, p, q)
        if left and right:
            return root
        return left or right
