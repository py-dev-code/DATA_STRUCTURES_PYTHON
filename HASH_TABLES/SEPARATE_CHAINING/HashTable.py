class HashTableSeparateChaining(object):

    '''
    A Hash Table implementation by using normal Python List. Method supports for functions like:
    Inserting Key, Removing Key, Getting Key, Checking the size, Iterating through all the keys etc.
    Class allows to define a custom Hash Function, Initial List Capacity and Load Factor.
    '''
    
    def __init__(self, capacity = None, load_factor = None, hash_function = None):
        
        def default_hash(key):
            result = 0
            if isinstance(key, str):
                for r in key:
                    result += ord(r)
            return result
        
        if capacity is not None and capacity < 0:
            raise ValueError("Invalid Capacity")
        if load_factor is not None and not (load_factor > 0 and load_factor < 1):
            raise ValueError("Invalid Load Factor")
        
        self.capacity = capacity if capacity is not None else 10
        self.load_factor = load_factor if load_factor is not None else 0.75
        self.hash_function = hash_function if hash_function is not None else default_hash
        self.size = 0
        self.data = [None] * self.capacity

    def insert_key(self, key, value):
        if key is None:
            raise Exception("Key cannot be None")
        index = self.hash_function(key) % self.capacity 

        if self.data[index] is None:
            self.data[index] = [[key, value]]
            self.size += 1
        else:
            if key in [x[0] for x in self.data[index]]:
                for i, r in enumerate(self.data[index]):
                    if r[0] == key:
                        self.data[index][i][1] = value
            else:
                self.data[index].append([key, value])
                self.size += 1

        if self.size > int(self.capacity * self.load_factor):
            self.resize_table()

    def resize_table(self):
        
        self.capacity *= 2
        new_data = [None] * self.capacity
        
        for r in self.data:
            if r is not None:
                for vals in r:
                    index = self.hash_function(vals[0]) % self.capacity

                    if new_data[index] is None:
                        new_data[index] = [[vals[0], vals[1]]]                        
                    else:
                        # No Need to handle the Duplicate Key case here
                        new_data[index].append([vals[0], vals[1]])
        
        self.data = new_data

    def get_key(self, key):
        if key is None:
            return None
        index = self.hash_function(key) % self.capacity
        try:
            list_index = [x[0] for x in self.data[index]].index(key)
        except:
            return None
        return self.data[index][list_index][1]
        
    def remove_key(self, key):
        if key is None:
            return None

        if not self.contains_key(key):
            raise KeyError("Key not found!")

        value = self[key]
        index = self.hash_function(key) % self.capacity            
        list_index = [x[0] for x in self.data[index]].index(key)            
        list_elem = self.data[index][list_index]
        self.data[index].remove(list_elem)
        self.size -= 1
    
        return value

    def __repr__(self):
        result = ""
        for i, _ in enumerate(self.data):
            if self.data[i] is not None:
                for r in self.data[i]:
                    result += str(r)+"\n"
        return result

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self.get_key(key)

    def __setitem__(self, key, value):
        self.insert_key(key, value)

    def __delitem__(self, key):
        return self.remove_key(key)

    def __contains__(self, key):
        return self.contains_key(key)

    def __iter__(self):
        for i, _ in enumerate(self.data):
            if self.data[i] is not None:
                for r in self.data[i]:
                    yield r[0]

    def isEmpty(self):
        return self.size == 0

    def clear(self):
        for key in list(self):
            self.remove_key(key)

    def contains_key(self, key):
        if key in list(self):
            return True
        return False

if __name__ == "__main__":
    h = HashTableSeparateChaining()
    print(h.capacity)           # 10
    for r in range(3):
        h[f'A{r}'] = 1
        h[f'B{r}'] = 2
        h[f'C{r}'] = 3
    h['A2'] = 100
    print(h.capacity)           # 20
    print(h)
    # ['A0', 1]
    # ['B0', 2]
    # ['A1', 1]
    # ['C0', 3]
    # ['B1', 2]
    # ['A2', 100]
    # ['C1', 3]
    # ['B2', 2]
    # ['C2', 3]
    print(h.remove_key('A2'))   # 100  
    print(f'Length: {len(h)}, {h.capacity}')
    # Length: 8, 20
    print(h['A2'])              # None
    for r in h:
        print(r)
    # A0
    # B0
    # A1
    # C0
    # B1
    # C1
    # B2
    # C2
    print(h.contains_key('A1')) # True
    h.clear()
    print(h.isEmpty())          # True
    


