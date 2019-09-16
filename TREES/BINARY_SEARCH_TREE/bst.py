import print_tree

class Node(object):
    
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.data)

class BinarySearchTree(object):
    
    def __init__(self, key = None):
        if key is None:
            self.root = None
        else:
            self.root = Node(key)

    def insert_key_bst(self, key):
        self.root = self.insert_key(self.root, key)

    def insert_key(self, root, key):
        if root is None:
            return Node(key)
        if root.data < key:
            root.right = self.insert_key(root.right, key)
        else:
            root.left = self.insert_key(root.left, key)
        return root

    def remove_key_bst(self, key):
        self.root = self.remove_key(self.root, key)

    def remove_key(self, root, key):
        if root is None: return

        if root.data < key:
            root.right = self.remove_key(root.right, key)
        elif root.data > key:
            root.left = self.remove_key(root.left, key)
        else:
            # Case 1,2 and 3: Either 1 child is None or both children are None
            if root.left is None:
                node = root.right
                root = None
                return node
            elif root.right is None:
                node = root.left
                root = None
                return node
            # Case 4: Both children are not None.
            # Root data will be replaced with its successor node (left most node in right subtree)
            # Once done, successor will be deleted from right subtree by using Case 1,2 and 3.
            else:
                successor = root.right
                while successor:
                    successor = successor.left
                root.data = successor.data
                root.right = self.remove_key(root.right, successor.data)
        # return the root to its calling method.
        return root

    def __len__(self):
        result = [0]
        self.get_node_count(self.root, result)
        return result[0]
    
    def get_node_count(self, root, result):
        if root is None: return
        self.get_node_count(root.left, result)
        result[0] += 1
        self.get_node_count(root.right, result)        
            
    def isEmpty(self):
        return len(self) == 0

    def min_node(self):
        node = self.root
        while node.left:
            node = node.left
        return node

    def max_node(self):
        node = self.root
        while node.right:
            node = node.right
        return node

    def contains(self, key):
        return self.contains_key(self.root, key)
    
    def contains_key(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        else:
            return self.contains_key(root.left, key) or self.contains_key(root.right, key)

    def height(self):
        return self.node_height(self.root)

    def node_height(self, root):
        if root is None:
            return 0
        return max(self.node_height(root.left), self.node_height(root.right)) + 1

    def pre_order_traverse(self, root):
        if root is None: return

        self.pre_order_traverse(root.left)
        print(root, end = ' ')
        self.pre_order_traverse(root.right)
        
    def post_order_traverse(self, root):
        if root is None: return
        
        self.post_order_traverse(root.right)
        print(root, end = ' ')
        self.post_order_traverse(root.left)
        
    def in_order_traverse(self, root):
        if root is None: return
        
        print(root, end = ' ')
        self.in_order_traverse(root.right)        
        self.in_order_traverse(root.left)
        
    def level_order_traverse(self):
        h = self.height()
        if h == 0: return
        for r in range(1, h + 1):
            self.traverse_level(r)
            print()

    def traverse_level(self, level):
        print(f'Level {level}: ', end = '')
        self.traverse_level_root(self.root, level)

    def traverse_level_root(self, root, level):  
        if root is None: return
        if level == 1:
            print(root, end = ' ')
        else:
            self.traverse_level_root(root.left, level - 1)
            self.traverse_level_root(root.right, level - 1)

    def print_tree(self):
        pass

if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in [1,2,3,4,5,6,7,8]: 
    # for i in [4,2,6,1,3,5,7,0]: 
        bst.insert_key_bst(i)

    bst.remove_key_bst(7)

    bst.post_order_traverse(bst.root)           # 8 6 5 4 3 2 1
    print()

    print(len(bst))                             # 7 
    print(bst.isEmpty())                        # False
    print(bst.min_node())                       # 1
    print(bst.max_node())                       # 8
    print(bst.contains(1), bst.contains(10))    # True False
    print(bst.height())                         # 7
    bst.level_order_traverse()
    # Level 1: 1
    # Level 2: 2
    # Level 3: 3
    # Level 4: 4
    # Level 5: 5
    # Level 6: 6
    # Level 7: 8
    print("======================================================")
    print_tree.print_tree(bst.root, bst.height(), max_node_len = 1)

