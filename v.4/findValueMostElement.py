import numpy as np
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes

if __name__ == "__main__":
    input = [1, 3, 2, 5, 3, np.nan, 9]
    s = Solution()
    print(s.largestValues(input))