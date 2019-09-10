class Node(object):
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

    def __repr__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self, values = None):
        self.head = None
        self.tail = None
        if values is not None:
            for r in values:
                self.add_in_end(r)    

    def add_in_end(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def add_in_start(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, self.head)

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def isEmpty(self):
        return len(self) == 0

    def remove_first(self):
        if self.isEmpty(): raise Exception("List is Empty")

        data = self.head.data
        self.head = self.head.next

        if self.isEmpty():
            self.head = self.tail = None
        
        return data

    def indexOf(self, node):
        
        idx = 0
        n = self.head

        while n:
            if n == node:
                return idx
            n = n.next
            idx += 1

        return -1

    def contains(self, node):
        return self.indexOf(node) != -1

class Stack(object):
    def __init__(self):
        self.ll = LinkedList()

    def __len__(self):
        return len(self.ll)

    def __repr__(self):
        return str(self.ll)

    def push(self, value):
        self.ll.add_in_start(value)

    def pop(self):
        if len(self.ll) == 0:
            raise Exception("Stack is Empty.") 
        return self.ll.remove_first()

    def peek(self):
        if len(self.ll) == 0:
            raise Exception("Stack is Empty.") 
        return self.ll.head

    def contains(self, node):
        return self.ll.contains(node)  

    def isEmpty(self):
        return len(self.ll) == 0

if __name__ == "__main__":
    s = Stack()
    
    for i in [1,2,3,4,5]:
        s.push(i)
    
    print(s)                # 5 -> 4 -> 3 -> 2 -> 1
    print(s.pop())          # 5
    print(s)                # 4 -> 3 -> 2 -> 1
    print(s.peek())         # 4
    print(s.contains(s.peek().next.next))    # Searching for node 2
    # True
    print(s.isEmpty())