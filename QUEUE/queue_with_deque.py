from collections import deque

class Queue(object):

    def __init__(self):
        self.d = deque()

    def __repr__(self):
        return ','.join([str(x) for x in list(self.d)])

    def __len__(self):
        return len(self.d)

    def isEmpty(self):
        return len(self.d) == 0

    def contains(self, value):
        return value in self.d
    
    def _enqueue(self, value):
        self.d.append(value)

    def _dequeue(self):
        if len(self.d) == 0:
            raise Exception("Queue is Empty.")
        return self.d.popleft()

    def peek(self):
        if len(self.d) == 0:
            raise Exception("Queue is Empty.")        
        return self.d[0]

if __name__ == "__main__":
    q = Queue()
    
    for i in [1,2,3,4,5]:
        q._enqueue(i)
    
    print(q)                # 1,2,3,4,5
    print(q._dequeue())     # 1
    print(q)                # 2,3,4,5
    print(q.peek())         # 2
    print(q.contains(5))    # True
    print(q.isEmpty())      # False  