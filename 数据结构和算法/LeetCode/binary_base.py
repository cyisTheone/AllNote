from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    q = deque([root])
    idx = 1
    while q and idx < len(nums):
        node = q.popleft()
        # 左孩子
        if nums[idx] is not None:
            node.left = TreeNode(nums[idx])
            q.append(node.left)
        idx += 1
        # 右孩子
        if idx < len(nums) and nums[idx] is not None:
            node.right = TreeNode(nums[idx])
            q.append(node.right)
        idx += 1
    return root


# 后序递归遍历， 36 37 38行的位置决定了前中后序遍历，现在是后序遍历，即： 右->中->左
def parser_tree(root, res):
    if not root:
        return
    parser_tree(root.right, res)
    parser_tree(root.left, res)
    res.append(root.val)


def levelOrder(root):
    # 层序遍历二叉树
    if not root:
        return
    dq = deque([root])
    while dq:
        for _ in range(len(dq)):
            curr = dq.popleft()
            print(curr.val, end=" ")
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, None])
    res = []
    parser_tree(root, res)
    print(res)
    levelOrder(root)
