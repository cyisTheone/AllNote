class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_traverse(root):
    """
    前序遍历，根左右
    使用栈来实现，先将根入栈，弹出并打印
    如果存在右节点，入栈，如果存在左节点，入栈。 先入右节点再入左节点，才能保证弹出的时候先去到左节点，再取到右节点

    """
    if not root:
        return

    stack = [root]

    while stack:
        # 第一步，弹出根节点
        node = stack.pop()
        print(node.val, end=" ")

        # 先将右节点入栈，再将左节点入栈
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def middle_traverse(root):
    """
    中序遍历， 左中右
    先将左子树全部入栈，然后弹出
    """
    if not root:
        return

    stack = []
    curr = root
    while stack or curr:
        # 向左遍历，知道curr的left为空
        while curr:
            stack.append(curr)
            curr = curr.left
        # 外层循环开始弹出元素
        curr = stack.pop()
        print(curr.val, end=" ")
        # 将当前节点的右节点赋值给curr，然后入栈（44行的while循环执行）
        curr = curr.right


def end_traverse(root):
    """
    后序遍历，参考中序遍历
    """
    if not root:
        return

    curr = root
    stack = []
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()
        print(curr.val, end=" ")

        curr = curr.left

if __name__ == "__main__":
    # 手动插入5个节点
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(7)

    print("前序遍历")
    pre_traverse(root)
    print("\n中序遍历")
    middle_traverse(root)
    print("\n后序遍历")
    end_traverse(root)
