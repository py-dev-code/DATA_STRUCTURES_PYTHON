class BinaryHeap(object):
    '''
    A Min Priority Queue implementation by using Binary Heap.
    '''

    def __init__(self, unsorted_list = None):
        self.array = []
        self.size = 0
        if unsorted_list is not None:
            self.heapify(unsorted_list)

    def heapify(self, ul):
        # Algorithm for Heapify:
        # First, we will take the input Unsorted List and create the data for our Heap.
        # Now, as we know that half of the Heap elements will be in the last level so 
        # we will loop through 2nd last level and apply sink mechanism on each of those 
        # elements to create the final Heap data in reverse order.
        # This whole process takes O(n) time after some mathematical analysis.
        # http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
        self.size = len(ul)
        self.array.extend(ul)        
        num_of_nodes = self.size // 2
        for r in reversed(range(num_of_nodes)):
            self.sink(r)

    def add_element(self, value):
        if value is None:
            raise ValueError("A Null Element cannot be inserted in the Heap.")
        self.array.append(value)
        self.size += 1
        self.swim(len(self.array) - 1)
        
    def swim(self, index):
        if index == 0: return
        # Find the Parent Node
        parent_index = (index - 1) // 2
        while self.array[parent_index] > self.array[index]:
            # swapping the values
            temp = self.array[parent_index]
            self.array[parent_index] = self.array[index]
            self.array[index] = temp
            self.swim(parent_index)

    def peek(self):
        if len(self.array) == 0: return None
        return self.array[0]

    def poll(self):
        return self.removeAt(0)

    def remove(self, value):
        try:
            index = self.array.index(value)
        except ValueError:
            raise ValueError(f'{value} is not in the heap.')
        self.removeAt(index)

    def removeAt(self, index):        
        # swapping the index element with last element
        temp = self.array[index]
        self.array[index] = self.array[self.size - 1]
        self.array[self.size - 1] = temp
        self.array.remove(self.array[self.size - 1])
        self.size -= 1
        self.sink(index)        
        return temp

    def sink(self, index):
        # Find both child node
        left_child = (index * 2) + 1
        right_child = left_child + 1

        if left_child > self.size - 1: return
        if right_child > self.size - 1 or self.array[left_child] <= self.array[right_child]: 
            child_index = left_child
        else:
            child_index = right_child

        while self.array[child_index] < self.array[index]:
            # swapping the values
            temp = self.array[child_index]
            self.array[child_index] = self.array[index]
            self.array[index] = temp
            self.sink(child_index)

    def __repr__(self):
        return ', '.join([str(x) for x in self.array])

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def contains(self, value):
        return value in self.array

    def is_min_heap_array(self, arr):
        return self.is_min_heap(0, arr)

    def is_min_heap(self, index, arr):
        n = len(arr) - 1 
        if index > n: return True
        left_child = (index * 2) + 1
        right_child = left_child + 1

        # Comparison
        if left_child <= n and arr[index] > arr[left_child]: return False
        if right_child <= n and arr[index] > arr[right_child]: return False

        return self.is_min_heap(left_child, arr) and self.is_min_heap(right_child, arr)

if __name__ == "__main__":
    heap = BinaryHeap([4,3,2,1,0,5,6,7,8])
    print(heap.poll())  # 0
    print(heap)
    # 1, 2, 3, 4, 8, 5, 6, 7
    print(heap.poll())  # 1
    print(heap)  
    # 2, 4, 3, 7, 8, 5, 6
    heap.remove(4)    
    print(heap)    
    # 2, 6, 3, 7, 8, 5
    print(heap.is_min_heap_array([3, 4, 5, 7, 8, 6]))      
    # True
    print(heap.size, len(heap)) 
    # 6 6
    print(heap.contains(60))
    # False
