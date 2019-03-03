class Solution1:
    def lowestCommonAncestor1(self, root, p, q):
        if root is None:
            return 
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor1(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor1(root.right, p, q)
        return root

class Solution2(object):
    def lowestCommonAncestor2(self, root, p, q):
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val <q.val:
                root = root.right
            else:
                return root
