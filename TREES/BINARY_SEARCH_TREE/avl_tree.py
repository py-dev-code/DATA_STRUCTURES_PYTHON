from print_tree import print_tree

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
        self.height = 1
    def __repr__(self):
        return str(self.data)

class AVLTree(object):
    
    def __init__(self, key = None):
        if key is None:
            self.root = None
            self.node_count = 0
        else:
            self.root = Node(key)
            self.node_count = 1
    
    def insert_key_avl(self, key):
        self.root = self.insert_key(self.root, key)

    def insert_key(self, root, key):
        if root is None:
            return Node(key)
        if root.data < key:
            root.right = self.insert_key(root.right, key)
        else:
            root.left = self.insert_key(root.left, key)

        l_height = 0 if root.left is None else root.left.height
        r_height = 0 if root.right is None else root.right.height
        root.height = max(l_height, r_height) + 1

        return self.balance_node(root, key)

    def remove_key_avl(self, key):
        return self.remove_key(self.root, key)

    def remove_key(self, root, key):
        if root is None: return

        if root.data > key:
            root.left = self.remove_key(root.left, key)
        elif root.data < key:
            root.right = self.remove_key(root.right, key)
        else:
            # case1,2,3: 1 child is None or both child are None
            if root.left is None:
                node = root.right
                return node
            elif root.right is None:
                node = root.left
                return node
            else:
                # case4: Cheat case: Find the successor, give its data to root and remove the successor.
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.data = successor.data
                root.right = self.remove_key(root.right, successor.data)
        return root                

    def balance_node(self, root, key):
        l_height = 0 if root.left is None else root.left.height
        r_height = 0 if root.right is None else root.right.height
        bf = l_height - r_height

        if bf == 2 and root.left.data > key:
            # left-left case
            return self.rotate_right(root)
        elif bf == -2 and root.right.data < key:
            # right-right case
            return self.rotate_left(root)
        elif bf == 2 and root.left.data < key:
            # left-right case
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        elif bf == -2 and root.right.data > key:
            # right-left case
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        else:
            return root

    def rotate_left(self, root):
        node = root.right
        root.right = node.left
        node.left = root
        return node

    def rotate_right(self, root):
        node = root.left
        root.left = node.right
        node.right = root
        return node             

if __name__ == "__main__":
    avl = AVLTree()
    for r in [1,2,3,4,5,6,7,8]:
        avl.insert_key_avl(r)
    avl.remove_key_avl(7)
    print_tree(avl.root, avl.root.height, 2)
    print("###############")
    avl.remove_key_avl(8)
    print_tree(avl.root, avl.root.height, 2)
    print("###############")
    avl.remove_key_avl(4)    
    print_tree(avl.root, avl.root.height, 2)
    print("###############")