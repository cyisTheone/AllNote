"""
翻转二叉树
"""
import collections
from typing import Optional
from binary_base import build_tree, levelOrder


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        dq = collections.deque([root])

        while dq:
            curr = dq.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)

        return root

if __name__ == "__main__":
    root = build_tree([4,2,7,1,3,6,9])
    S = Solution()
    res1 = S.invertTree(root)
    levelOrder(res1) # output [4,7,2,9,6,3,1]
