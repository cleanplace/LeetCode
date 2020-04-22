# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        nodes = [root] if root else []

        while nodes:
            next_nodes = []
            last = None

            for node in nodes:
                if last:
                    last.next = node
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
                last = node
            nodes = next_nodes

        return root