from collections import deque

class Stack(object):

    def __init__(self):
        self.d = deque()        

    def __len__(self):
        return len(self.d)

    def __repr__(self):
        return ','.join([str(x) for x in list(self.d)])

    def push(self, value):
        self.d.appendleft(value)

    def pop(self):
        if len(self.d) == 0:
            raise Exception("Stack is Empty.")
        return self.d.popleft()

    def peek(self):
        if len(self.d) == 0:
            raise Exception("Stack is Empty.")        
        return self.d[0]

    def contains(self, value):
        return value in self.d

    def isEmpty(self):
        return len(self.d) == 0

if __name__ == "__main__":
    s = Stack()
    
    for i in [1,2,3,4,5]:
        s.push(i)
    
    print(s)                # 5,4,3,2,1
    print(s.pop())          # 5
    print(s)                # 4,3,2,1
    print(s.peek())         # 4
    print(s.contains(1))    # True
    print(s.isEmpty())
