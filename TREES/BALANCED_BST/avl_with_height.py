# from print_tree import print_tree

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
        self.height = 1
    def __repr__(self):
        return f'{self.data},{self.height}'

class AVLTree(object):
    
    def __init__(self):
        self.root = None

    def update_height(self, node):
        if node is None: return
        l_height = 0 if node.left is None else node.left.height
        r_height = 0 if node.right is None else node.right.height
        node.height = max(l_height, r_height) + 1

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

    def add_value_bst(self, value):
        def add_value_bst_util(root, value):
            if root is None:
                return Node(value)
            if root.data >= value:
                root.left = add_value_bst_util(root.left, value)                
            else:
                root.right = add_value_bst_util(root.right, value)
            self.update_height(root)
            return self.balance(root)                
        
        self.root = add_value_bst_util(self.root, value)  

    def remove_value_bst(self, value):
        def remove_value_bst_util(root, value):
            if root is None: return
            if root.data > value:
                root.left = remove_value_bst_util(root.left, value)
            elif root.data < value:
                root.right = remove_value_bst_util(root.right, value)
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
            self.update_height(root)        
            return self.balance(root)
            
        if self.find_value(value):
            self.root = remove_value_bst_util(self.root, value)
        else:
            raise ValueError("Value not Present")
    
    def balance(self, root):
        def height(root):
            return 0 if root is None else root.height

        def rotate_right(root):
            if root is None: return
            node = root.left
            root.left = node.right
            self.update_height(root)
            node.right = root
            self.update_height(node)
            return node

        def rotate_left(root):
            if root is None: return
            node = root.right
            root.right = node.left
            self.update_height(root)
            node.left = root
            self.update_height(node)
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
    # (avl.root, avl.get_height(), 2)
    avl.remove_value_bst(5)
    avl.print_tree()
    # print_tree(avl.root, avl.get_height(), 2)
    print("###############")
    avl.remove_value_bst(7)
    avl.print_tree()
    # print_tree(avl.root, avl.get_height(), 2)
    print("###############")
    avl.remove_value_bst(8)
    avl.print_tree()
    # print_tree(avl.root, avl.get_height(), 2)
    print("***************")
    avl.remove_value_bst(3)    
    avl.print_tree()
    # print_tree(avl.root, avl.get_height(), 2)
    print("###############")
    avl.remove_value_bst(4)    
    avl.print_tree()
    # print_tree(avl.root, avl.get_height(), 2)
    