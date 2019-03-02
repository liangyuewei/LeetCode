## 深度优先算法

## 递归算法
visited = set()
def dfs(node, visited):
    visited.add(node)
    for node_next in node.children():
        if not node_next in visited:
            dfs(node_next, visited)

## 非递归算法
def dfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)
    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        nodes = genetrate_relted_nodes(node)
        queue.push(nodes)