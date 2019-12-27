from random import randint

'''
    AVL Tree can be implemented similar to a Binary Search Tree. 
    Only change is that each node in AVL Tree maintain its Height and on Insert/Removal 
    of a Key, we need to balance the nodes.
    Therefore, below implementation shows only insert and remove methods.
    Rest all methods will be exactly same as BST methods.
'''
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.left_nodes = 0
        self.right_nodes = 0
    def __repr__(self):
        return f'{self.data},{self.left_nodes},{self.right_nodes}'

class AVLTree(object):
    
    def __init__(self):
        self.root = None

    def height(self):
        def height_util(root):
            if root is None:
                return 0
            else:
                return max(height_util(root.left), height_util(root.right)) + 1
        return height_util(self.root)       

    def find_value(self, value):
        def find_value_util(root, util):
            if root is None:
                return False
            if root.data == value:
                return True
            elif root.data > value:
                return find_value_util(root.left, value)
            else:
                return find_value_util(root.right, value)
        return find_value_util(self.root, value)

    def get_random_node(self):
        def get_random_node_util(root):
            root_size = root.left_nodes + root.right_nodes + 1
            left_size = 0 if root.left is None else root.left.left_nodes + root.right.right_nodes + 1
            random_num = randint(1,root_size)
            if random_num == root_size:
                return root
            elif random_num <= left_size:
                return get_random_node_util(root.left)
            else:
                return get_random_node_util(root.right)

        if self.root is None: return
        return get_random_node_util(self.root)

    def add_value_bst(self, value):
        def add_value_bst_util(root, value):
            if root is None:
                return Node(value)
            if root.data >= value:
                root.left = add_value_bst_util(root.left, value)
                root.left_nodes += 1
            else:
                root.right = add_value_bst_util(root.right, value)
                root.right_nodes += 1
            return self.balance(root)                
        
        self.root = add_value_bst_util(self.root, value)  

    def remove_value_bst(self, value):
        def remove_value_bst_util(root, value):
            if root is None: return
            if root.data > value:
                root.left = remove_value_bst_util(root.left, value)
                root.left_nodes -= 1
            elif root.data < value:
                root.right = remove_value_bst_util(root.right, value)
                root.right_nodes -= 1
            else:
                # No child / Only 1 Child
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                # Both Child case
                else:
                    node = root.right
                    while node.left:
                        node = node.left
                    root.data = node.data
                    node.data = value
                    root.right = remove_value_bst_util(root.right, value)
                    root.right_nodes -= 1
            return self.balance(root)
        if self.find_value(value):    
            self.root = remove_value_bst_util(self.root, value)
        else:
            raise ValueError("Value not Present")
    
    def balance(self, root):
        def height(root):
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1

        def rotate_right(root):
            if root is None: return
            node = root.left
            root.left = node.right
            if node.right:
                nodes = node.right.left_nodes + node.right.right_nodes + 1 
            else:
                nodes = 0
            root.left_nodes = nodes
            node.right = root
            node.right_nodes = root.left_nodes + root.right_nodes + 1
            return node

        def rotate_left(root):
            if root is None: return
            node = root.right
            root.right = node.left
            if node.left:
                nodes = node.left.left_nodes + node.left.right_nodes + 1
            else:
                nodes = 0
            root.right_nodes = nodes
            node.left = root
            node.left_nodes = root.left_nodes + root.right_nodes + 1
            return node

        if root is None: return
        lh = height(root.left)
        rh = height(root.right)

        if lh - rh > 1:
            if root.left.left is not None:
                return rotate_right(root)                
            else:
                root.left = rotate_left(root.left)
                return rotate_right(root)
        elif rh - lh > 1:
            if root.right.right is not None:
                return rotate_left(root)                
            else:
                root.right = rotate_right(root.right)
                return rotate_left(root)
        return root

    def print_tree(self, max_node_len=2):
        print_tree(self.root, max_node_len)

def print_tree(root, max_node_len=2):
    def get_root_height(root):
        if root is None: return 0
        return max(get_root_height(root.left), get_root_height(root.right)) + 1
    def get_parents(level, nodes):
        return nodes[2**level - 1: 2**(level+1) - 1]
    def process_level(root, level, nodes):
        node_length = line_length // (2**level)
        if level == 0:
            nodes.append(root)
            print_value = str(root.data)
            print(print_value.center(node_length, ' '), end='')
        else:
            for r in get_parents(level - 1, nodes):
                value = 'X' if r == 'X' or r.left is None else r.left
                print_value = '' if value == 'X' else str(value.data)
                nodes.append(value)
                print(print_value.center(node_length, ' '), end='')

                value = 'X' if r == 'X' or r.right is None else r.right
                print_value = '' if value == 'X' else str(value.data)
                nodes.append(value)
                print(print_value.center(node_length, ' '), end='')        
    if root is None: return
    height = get_root_height(root)
    line_length = 2**(height-1) * 2 * max_node_len
    nodes = []
    for level in range(height):
        process_level(root, level, nodes)
        print()       
    print(root,'|', root.left, '|', root.right) 

if __name__ == "__main__":
    avl = AVLTree()
    for r in [1,2,3,4,5,6,7,8]:
        avl.add_value_bst(r)
    avl.print_tree()
    avl.remove_value_bst(5)
    avl.print_tree()
    print("###############")
    avl.remove_value_bst(7)
    avl.print_tree()
    print("###############")
    avl.remove_value_bst(8)
    avl.print_tree()
    print("***************")
    avl.remove_value_bst(3)    
    avl.print_tree()
    print("***************")
    avl.remove_value_bst(4)    
    avl.print_tree()
    
    print("***************")
    print("Random Nodes")
    for r in range(10):
        print(avl.get_random_node())
    
    