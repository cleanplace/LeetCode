# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = TreeNode(data)
        else:
            node.left = self._insert_value(node.left, data)
            node.right = self._insert_value(node.right, data)

        return node



if __name__ == "__main__":
    input_list = [4, 2, 7, 1, 3, 6, 9]

    bst = BinarySearchTree()
    for x in input_list:
        bst.insert(x)

    #print(bst)

    s = Solution()
    result = s.invertTree(bst)

    print(result)