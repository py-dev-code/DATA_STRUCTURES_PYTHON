class Node(object):
    def __init__(self, value, prev = None, next = None):
        self.data = value
        self.prev = prev
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
            self.tail.next = Node(value, self.tail, None)
            self.tail = self.tail.next

    def add_in_start(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, None, self.head)
            self.head.next.prev = self.head

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        values = [str(x) for x in self]
        return ' <-> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def clear(self):
        n = self.head
        while n:
            next = n.next
            n = None
            n = next
        self.head = self.tail = n = None

    def isEmpty(self):
        return len(self) == 0

    def remove_first(self):
        if self.isEmpty(): raise Exception("List is Empty")

        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None

        if self.head is None:
            self.head = self.tail = None
        
        return data

    def remove_last(self):
        if self.isEmpty():
            raise Exception("List is Empty")

        data = self.tail.data        
        if self.head == self.tail:
            self.head = self.tail = None
            return data
            
        self.tail = self.tail.prev   

        if self.tail:
            self.tail.next = None
            
        if self.isEmpty():
            self.head = self.tail = None        

    def remove(self, node):
        
        if node == self.head:
            return self.remove_first()
        if node == self.tail:
            return self.remove_last()

        data = node.data

        node.prev.next = node.next
        node.next.prev = node.prev

        return data

    def removeAt(self, index):
        if index < 0 or index >= len(self):
            raise Exception("Index out of Bound.")
        
        idx = 0
        n = self.head        
        while n:
            if idx == index:
                return self.remove(n)
            n = n.next
            idx += 1

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

if __name__ == "__main__":
    ll = LinkedList('abcdef')
    print(ll)       # a <-> b <-> c <-> d <-> e <-> f
    print(len(ll))  # 6

    # Forward Traversing
    h = ll.head
    while h:
        print(f'{h} <->', end = ' ')
        h = h.next
    print()
    # a <-> b <-> c <-> d <-> e <-> f <->

    # Backward Traversing
    t = ll.tail
    while t:
        print(f'{t} <->', end = ' ')
        t = t.prev
    print()
    # f <-> e <-> d <-> c <-> b <-> a <->

    e = ll.remove_first()
    print(f'{e}, {ll}, {len(ll)}')
    # a, b <-> c <-> d <-> e <-> f, 5

    e = ll.remove_last()
    print(f'{e}, {ll}, {len(ll)}')
    # f, b <-> c <-> d <-> e, 4

    e = ll.remove(ll.head.next.next)    # removing node d
    print(f'{e}, {ll}, {len(ll)}')
    # d, b <-> c <-> e, 3

    e = ll.removeAt(1)
    print(f'{e}, {ll}, {len(ll)}')    
    # c, b <-> e, 2

    print(ll.indexOf(ll.head.next))
    # 1
    print(ll.contains(Node('b')))
    # False

    ll.clear()
    print(len(ll), ll.head, ll.tail)
    print(ll.isEmpty())