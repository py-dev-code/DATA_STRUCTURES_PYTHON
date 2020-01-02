class Stack(object):
    class StackNode(object):
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    def __init__(self):
        self.top = None
    def pop(self):
        if self.top is None:
            raise ValueError("Stack is Empty")
        else:
            item = self.top.data
            self.top = self.top.next
            return item
    def push(self, item):
        if self.top is None:
            self.top = Stack.StackNode(item)
        else:
            self.top = Stack.StackNode(item, self.top)
    def peek(self):
        if self.top is None:
            raise ValueError("Stock is Empty")
        else:
            return self.top.data
    def isEmpty(self):
        return self.top is None
    def __repr__(self):
        result = []
        node = self.top
        while node:
            result.append(str(node.data))
            node = node.next
        return ' <- '.join(result)