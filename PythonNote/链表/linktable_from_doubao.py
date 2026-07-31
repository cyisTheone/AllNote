class ListNode:
    """链表节点"""
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # 头结点
    
    def add_at_head(self, val):
        """头部插入"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, val):
        """尾部追加"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def add_at_index(self, index, val):
        """指定下标插入（下标从0开始）"""
        if index == 0:
            self.add_at_head(val)
            return
        cur = self.head
        # 找到index-1位置
        for _ in range(index - 1):
            if not cur:  # 下标越界
                return
            cur = cur.next
        if not cur:
            return
        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node

    def get(self, index):
        """查询：按下标取值，不存在返回None"""
        cur = self.head
        for _ in range(index):
            if not cur:
                return None
            cur = cur.next
        return cur.val if cur else None

    def update(self, index, new_val):
        """修改：指定下标节点值"""
        cur = self.head
        for _ in range(index):
            if not cur:
                return False
            cur = cur.next
        if cur:
            cur.val = new_val
            return True
        return False

    def delete_at_index(self, index):
        """按下标删除节点"""
        if not self.head:
            return
        # 删除头节点
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        for _ in range(index - 1):
            if not cur.next:
                return
            cur = cur.next
        # cur.next 为待删节点
        cur.next = cur.next.next

    def print_list(self):
        """打印链表"""
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        print(" -> ".join(res))

    def is_empty(self):
        return self.head is None