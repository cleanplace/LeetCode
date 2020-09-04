# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search
class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans

# Bottom-up Recursion using Post-order Traversal
class Solution(object):
    def distributeCoins(self,r):
        ops = 0

        def dist(n):
            nonlocal ops

            l = dist(n.left) if n.left else 0
            r = dist(n.right) if n.right else 0
            n.val += (l + r)
            ops += abs(n.val - 1)
            return n.val - 1

        dist(r)

        return ops

if __name__ == "__main__":

    root = TreeNode(val=3,left=0, right=0)

    s = Solution()
    print(s.distributeCoins(root))