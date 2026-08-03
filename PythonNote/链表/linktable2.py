# 循环链表

class LinkNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def insert_node(root, val, next=None):

    if not root:
        return

    curr = root

    while curr.next:
        curr = curr.next

    curr.next = LinkNode(val)

def print_link(head):

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print("\n")

head = LinkNode(9)
for i in range(10, 15):
    insert_node(head, i)

print_link(head)


# 反转链表

# 定义前一个节点为空（未来的尾节点）
pre = None

# 定义当前节点为头结点，用这个来遍历链表
curr = head

while curr:
    # 记录当前遍历到的节点的next
    nxt = curr.next
    # 当前节点的下一个节点为pre
    curr.next = pre
    # 前一个节点置为当前节点
    pre = curr

    # 当前节点置为下一个节点
    curr = nxt

print_link(pre)

# 快慢指针寻找中间节点
fast = slow = pre
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

print(slow.val)

    