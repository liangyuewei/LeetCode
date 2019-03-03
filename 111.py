# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree[3, 9, 20, null, null, 15, 7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if root.left != None or root.right != None:
            return min(left, right) + 1
        else:
            return max(left, right) + 1