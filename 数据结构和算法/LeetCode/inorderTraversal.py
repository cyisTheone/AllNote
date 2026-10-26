# 二叉树中序遍历
import collections
from typing import Optional, List
from binary_base import build_tree, levelOrder


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5])
    S = Solution()
    res = S.inorderTraversal(root)
    levelOrder(res)

