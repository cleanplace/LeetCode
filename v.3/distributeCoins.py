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

            #nonlocal : 전역 변수도 아니고 지역변수도 아님. 사용된 함수의 바로 바깥쪽 함수까지만 변수에 영향을 주는 변수 선언방식
            #즉, nonlocal 이 사용된 함수 바로 한단계 바깥쪽에 위치한 변수와 바인딩을 할 수 있다.
            nonlocal ops

            l = dist(n.left) if n.left else 0
            r = dist(n.right) if n.right else 0
            n.val += (l + r) #후위 순회 방식 (왼쪽 자식 노드 -> 오른쪽 자식 노드 -> 부모 노드)

            ops += abs(n.val - 1) #노드마다 1개씩 배분해야하니깐 Recursion하게 호출되면서 가지고 있는 자산에서 -1씩함
            return n.val - 1

        dist(r)

        return ops

if __name__ == "__main__":

    root = TreeNode(val=3,left=0, right=0)

    s = Solution()
    print(s.distributeCoins(root))