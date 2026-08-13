"""
对称二叉树判断
"""

from typing import Optional
from binary_base import build_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(a, b):
            # 情况一：两个节点都为空，对称
            if not a and not b:
                return True
            # 情况二，有一个节点为空，不对称
            if not a or not b:
                return False
            # 节点值相等，且左节点等于右节点，右节点等于左节点
            return a.val == b.val and check(a.left, b.right) and check(a.right, b.left)

        if not root:
            return True
        return check(root.left, root.right)


if __name__ == "__main__":
    root = build_tree([1, 2, 2, 3, 4, 4, 3])
    S = Solution()
    res1 = S.isSymmetric(root)
    print(res1)  # True
