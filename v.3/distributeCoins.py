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
class Solution:
    def distributeCoins(self, r):
        ops = 0

        def _dist(n):
            nonlocal ops
            l = _dist(n.left) if n.left else 0
            r = _dist(n.right) if n.right else 0
            n.val += (l + r)
            ops += abs(n.val - 1)
            return n.val - 1

        _dist(r)
        return ops