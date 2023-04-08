"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        maximum_depth = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            maximum_depth = max(depth, maximum_depth)

            for node in node.children:
                stack.append((node, depth + 1))

        return maximum_depth
