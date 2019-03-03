# Given a binary tree, determine if it is a valid binary search tree(BST).
    # Assume a BST is defined as follows:

    # The left subtree of a node contains only nodes with keys less than the node's key.
    # The right subtree of a node contains only nodes with keys greater than the node's key.
    # Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return True
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

class Solution2:
    def isValidBST2(self, root):
        self.prev = None
        return self.helper(root)
    
    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)

class Solution3:
    def isValidBST3(self, root, min, max):
        if root is None:
            return True
        if min is not None and root.val <= min:
            return False
        if max is not None and root.val >= max:
            return False
        return self.isValidBST3(root.left, min, root.val) and self.isValidBST3(root.right, root.val, max)