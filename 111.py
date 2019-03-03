class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if root.left != None or root.right != None:
            return min(left, right) + 1
        else:
            return max(left, right) + 1