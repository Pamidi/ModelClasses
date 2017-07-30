class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, nd):
        if not self.head:
            self.head, self.tail = nd, nd
            return

        self.tail.next = nd
        self.tail = nd

    def display(self):
        cur = self.head

        while cur:
            print cur.val
            cur = cur.next