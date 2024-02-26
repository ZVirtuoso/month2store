"""
对链表的一些处理方法：打印，指定位置插入
"""
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        """打印链表中的元素,使用临时指针不会改变原链表"""
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    def insert_beginning(self, val):
        """在链表头部插入节点"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, val):
        """在链表尾部插入节点"""
        if self.head is None:
            self.head = ListNode(val)
            return
        new_node = self.head
        while new_node.next:
            new_node = new_node.next
        new_node.next = ListNode(val)

    def insert(self, val, index=0):
        """index:在第index个数据后插入新节点,默认0即为从头部插入"""
        if index == 0:
            self.insert_beginning(val)
            return
        new_node = self.head
        for i in range(index - 1):
            new_node = new_node.next
        insert_node = ListNode(val)  # 创建
        insert_node.next = new_node.next  # 传递
        new_node.next = insert_node  # 重置向
        # new_node.next = ListNode(val)#直接换后续链表消失
        # new_node.next.next = new_node.next


list = LinkedList()
list.head = ListNode("Monday")
e2 = ListNode("Tuesday")
e3 = ListNode("Wednesday")
list.head.next = e2
e2.next = e3
# list.insert_beginning("Sun")
# list.insert_end("Thursday")
list.insert("Tuesday_afternoon", 2)
list.print_list()
list.print_list()
