import numpy as np
# BFS + queue
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res

if __name__ == "__main__":
    #root = [5, 4, 8, 11, np.nan, 13, 4, 7, 2, np.nan, np.nan, 5, 1]
    sum = 22

    root = TreeNode()
    root.val = 5
    root.left = TreeNode()
    root.left.val = 4
    root.right = TreeNode()
    root.right.val = 8

    root.left.left = TreeNode()
    root.left.left.val = 11
    root.left.right= TreeNode()
    root.left.right.val = np.nan

    root.left.left.left = TreeNode()
    root.left.left.left.val = 7
    root.left.left.right = TreeNode()
    root.left.left.right.val = 2

    root.right.left = TreeNode()
    root.right.left.val = 13
    root.right.right = TreeNode()
    root.right.right.val = 4

    root.right.left.left = TreeNode()
    root.right.left.left.val = np.nan
    root.right.left.right = TreeNode()
    root.right.left.right.val = np.nan

    root.right.right.left = TreeNode()
    root.right.right.left.val = 5
    root.right.right.right = TreeNode()
    root.right.right.right.val = 1

    s = Solution()
    result = s.pathSum(root,sum)

    print(result)