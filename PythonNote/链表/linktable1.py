class LinkNode():
    # 定义链表
    def __init__(self, val):
        self.val = val
        self.next = None

# 插入节点，尾插
def insert_node(head, val):

    if head is None:
        return 

    new_node = LinkNode(val)

    curr = head
    while curr.next: # 等价于 while curr.next is not None: 当前节点的next指针域为空
        curr = curr.next

    curr.next = new_node


# 循环打印链表
def print_link(root):

    curr = root
    while curr: # 等价于 while curr is not None
        print(curr.val)
        curr = curr.next

if __name__ == "__main__":

    # 定义链表
    head = LinkNode(10)
    # 插入元素
    insert_node(head, 30)
    insert_node(head, 40)
    # 循环打印链表
    print_link(head)