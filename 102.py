class Solution01(object):
    def levelOrder(self, root):
        if not root: return []
        result = []
        import collections
        queue = collections.deque()
        queue.append(root)

        # visited = set()

        while queue:
            level_size = len(queue)
            currrnt_level = []

            for _ in range(level_size):
                node = queue.popleft()
                # visited.add(node)
                currrnt_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(currrnt_level)
        return result

class Solution02(object):
    def levelOrder(self, root):
        if not root: return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node: return 
        if len(self.result) < level + 1:
            self.result.append([])
        
        self.result[level].append(node.val)
        if node.left: self._dfs(node.left, level + 1)
        if node.right: self._dfs(node.right, level + 1)