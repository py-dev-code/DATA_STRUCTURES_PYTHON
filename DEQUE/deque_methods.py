from collections import deque

# deque are implemented as Doubly Linked List in Python so they are a good choice
# for a fast add and remove elements from head/tail of the list.

# Initiation
# deque([iterable, [maxlen]])

d = deque('abc')
for i in d: 
    print(i, end = ' ')
print()
# a b c

# append to right and left
d.append('d')
d.appendleft('e')
print(d)
# deque(['e', 'a', 'b', 'c', 'd'])

# Popping the element from right and left
print(d.pop())
# d
print(d.popleft())
# e

print(d)
# deque(['a', 'b', 'c'])

# Peeking from left and right
print(d[0], d[-1])
# a c

# converting into list
l1 = list(d)
l2 = list(reversed(d))
print(l1, l2, d)
# ['a', 'b', 'c'] ['c', 'b', 'a'] deque(['a', 'b', 'c'])

print(len(d))
# 3
print(d[0], d[1], d[2])
# a b c

d.extend('def')
print(d)
# deque(['a', 'b', 'c', 'd', 'e', 'f'])

d.rotate(1)     # right rotation
print(d)
# deque(['f', 'a', 'b', 'c', 'd', 'e'])

d.rotate(-1)    # left rotation
print(d)
# deque(['a', 'b', 'c', 'd', 'e', 'f'])

d.extendleft('xyz')
print(d)
# deque(['z', 'y', 'x', 'a', 'b', 'c', 'd', 'e', 'f'])

# empty the deque
d.clear()
print(d)
# deque([])
