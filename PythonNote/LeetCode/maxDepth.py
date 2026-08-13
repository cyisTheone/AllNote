"""
求二叉树最大深度
"""
import collections
from typing import Optional
from binary_base import build_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        层序遍历来求
        """
        if not root:
            return 0
        dq = collections.deque([root])
        depth = 0
        while dq:
            depth += 1
            for _ in range(len(dq)):

                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

        return depth

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        """
        递归法来求
        """
        if not root:
            return 0
        max_left = self.maxDepth1(root.left)
        max_right = self.maxDepth1(root.right)
        return max(max_left, max_right) + 1


if __name__ == "__main__":
    root = build_tree([3, 9, 20, None, None, 15, 7])
    S = Solution()
    res1 = S.maxDepth(root)
    print(res1)  # ouput 3

    res2 = S.maxDepth1(root)
    print(res2)  # oupt 3
