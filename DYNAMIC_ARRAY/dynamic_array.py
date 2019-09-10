import ctypes
# # ctypes is a foreign function library for Python. It provides C compatible data types, 
# # and allows calling functions in DLLs or shared libraries. 
# It can be used to wrap these libraries in pure Python.
'''
    Dynamic Array or Python List implementation
'''

class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()
        # ctypes.py_object:
        # Represents the C PyObject * datatype. Calling this without an argument creates a NULL PyObject * pointer.
        # PyObject:
        # All object types are extensions of this type. This is a type which contains the information Python needs to treat a pointer to an object as an object. In a normal “release” build, it contains only the object’s reference count and a pointer to the corresponding type object. Nothing is actually declared to be a PyObject, but every pointer to a Python object can be cast to a PyObject*. Access to the members must be done by using the macros Py_REFCNT and Py_TYPE.

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if k > self.n or k < 0:
            return IndexError('Out of Bound')
        return self.A[k]

    def append(self, element):
        if self.n == self.capacity:
            self.resize(self.capacity * 2)
        self.A[self.n] = element
        self.n += 1

    def resize(self, new_capacity):
        B = self.make_array(new_capacity)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B  # resetting the pointer
        self.capacity = new_capacity

if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(10)
    print(arr[0])   # 10
    print(len(arr)) # 1

    arr.append(2)
    print(len(arr)) # 2