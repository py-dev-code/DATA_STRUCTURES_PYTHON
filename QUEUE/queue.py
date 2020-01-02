class Queue(object):
    class QueueNode(object):
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    def __init__(self):
        self.first = None
        self.last = None
    def add(self, item):
        if self.first is None:
            self.first = self.last = Queue.QueueNode(item)
        else:
            node = Queue.QueueNode(item)
            self.last.next = node
            self.last = node
    def remove(self):
        if self.first is None:
            raise ValueError("Queue is Empty")
        else:
            item = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.first = self.last = None
            return item
    def peek(self):
        if self.first is None:
            raise ValueError("Queue is Empty")
        else:
            return self.first.data
    def isEmpty(self):
        return self.first is None
    def __repr__(self):
        result = []
        node = self.first
        while node:
            result.append(str(node.data))
            node = node.next
        return ' -> '.join(result)