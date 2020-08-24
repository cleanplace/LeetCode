class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        root=TreeNode(max(nums))
        index=nums.index(max(nums))
        root.left=self.constructMaximumBinaryTree(nums[:index])
        root.right=self.constructMaximumBinaryTree(nums[index+1:])
        return root

if __name__ == "__main__":

    input = [3,2,1,6,0,5]
    s = Solution()
    print(s.constructMaximumBinaryTree(input))