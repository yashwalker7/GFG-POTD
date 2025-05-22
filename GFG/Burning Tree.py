from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def find_node(self, root, target_data):
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.data == target_data:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None

    def build_parent_map(self, root):
        parent_map = {}
        queue = deque([root])
        parent_map[root] = None
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)
        return parent_map

    def minTime(self, root, target_data):
        target_node = self.find_node(root, target_data)
        if not target_node:
            return 0
        parent_map = self.build_parent_map(root)
        visited = set()
        queue = deque([target_node])
        visited.add(target_node)
        time = 0
        while queue:
            level_size = len(queue)
            burned = False
            for _ in range(level_size):
                node = queue.popleft()
                parent = parent_map.get(node)
                if parent and parent not in visited:
                    visited.add(parent)
                    queue.append(parent)
                    burned = True
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                    burned = True
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                    burned = True
            if burned:
                time += 1
        return time
