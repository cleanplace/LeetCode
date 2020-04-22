# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level = 0
        result = []
        parents = []
        currents = []
        if root:
            currents.append(root)
        while currents:
            tmp = []
            parents = currents
            currents = []
            for p in parents:
                tmp.append(p.val)
                if p.left:
                    currents.append(p.left)
                if p.right:
                    currents.append(p.right)

            result.append(tmp if level % 2 == 0 else tmp[::-1])
            level += 1

        return result