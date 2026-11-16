"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        cloned = {}
        
        def dfs(current: 'Node') -> 'Node':
            # If the node is already cloned, return its clone
            if current in cloned:
                return cloned[current]
            
            # Create a new clone for the current node
            copy = Node(current.val)
            cloned[current] = copy
            
            # Recursively clone all neighbors and add them to the clone's neighbors
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)