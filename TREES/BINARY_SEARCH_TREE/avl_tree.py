# from print_tree import print_tree

'''
    AVL Tree can be implemented similar to a Binary Search Tree. 
    Only change is that each node in AVL Tree maintain its Height and on Insert/Removal 
    of a Key, we need to balance the nodes.
    Therefore, below implementation shows only insert and remove methods.
    Rest all methods will be exactly same as BST methods.
'''
class Node(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.data)

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

    def add_value_bst(self, value):
        def add_value_bst_util(root, value):
            if root is None:
                return Node(value)
            if root.data >= value:
                root.left = add_value_bst_util(root.left, value)
            else:
                root.right = add_value_bst_util(root.right, value)
            return self.balance(root)                
        
        if self.root is None:
            self.root = Node(value)
        else:
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
            return self.balance(root)
            
        self.root = remove_value_bst_util(self.root, value)              
    
    def balance(self, root):
        def height(root):
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1

        def rotate_right(root):
            if root is None: return
            node = root.left
            root.left = node.right
            node.right = root
            return node

        def rotate_left(root):
            if root is None: return
            node = root.right
            root.right = node.left
            node.left = root
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

    def print_tree(self, node_length=2):
        def get_parent_level(nodes, level):
            return nodes[2**(level) - 1: 2**(level+1) - 1]

        def process_level(root, nodes, level, line_length):
            if root is None: return
            node_space = line_length // 2**(level)
            if level == 0:
                nodes.append(root)
                print(str(nodes[len(nodes) - 1]).center(node_space, ' '), end='')
            else:
                for parent in get_parent_level(nodes, level - 1):
                    if parent == 'X':
                        
                        value = 'X'
                        print_value = ''
                        nodes.append(value)
                        print(print_value.center(node_space, ' '), end='') 

                        value = 'X'
                        print_value = ''
                        nodes.append(value)
                        print(print_value.center(node_space, ' '), end='') 

                    else:
                        
                        value = 'X' if parent.left is None else parent.left
                        print_value = '' if parent.left is None else str(parent.left.data)
                        nodes.append(value)
                        print(print_value.center(node_space, ' '), end='')

                        value = 'X' if parent.right is None else parent.right
                        print_value = '' if parent.right is None else str(parent.right.data)
                        nodes.append(value)
                        print(print_value.center(node_space, ' '), end='')
        
        height = self.height()
        nodes = []
        line_length = 2**(height - 1) * 2 * node_length
        for l in range(height):
            process_level(self.root, nodes, l, line_length)
            print()        

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
    