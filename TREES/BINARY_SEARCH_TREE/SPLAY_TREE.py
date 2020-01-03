'''
Reference Link: https://algorithmtutor.com/Data-Structures/Tree/Splay-Trees/
Data Structure:
    1. Splay Tree is a type of Binary Search Tree that keeps the recently operated nodes at the root for 
    subsequent opertations. For ex: if we search a node, it will be moved to the root. This process is
    called Splaying. 
    2. When we insert a node, we insert it like a normal BST but then we splay the new node to the root.
    3. Splaying process is done via Right and Left Roations which are also called as Zig and Zag Operations.
    4. To delete a Node, we do 2 operations:
        Split the Tree: We Split the Tree at Node x (the node which needs to be deleted) into S and T.
        Once done, we remove node x from the Tree S which is at the root.
        Join the Tree: We join remaining S and T to have Node x deleted from the Tree.
    5. Most complicated operations in a Splay Tree is Splaying where we need to apply multiple rotations.
    6. We need to carefully apply the rotations as we need to maintatin Parent node link as well.
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    def __repr__(self):
        return str(self.data)

class SplayTree(object):
    def __init__(self):
        self.root = None
    
    def splay(self, node):
        while node.parent:
            if node.parent.parent is None:
                if node.parent.left == node:
                    # Zig Operation
                    self.right_rotate(node.parent)
                else:
                    # Zag Operation
                    self.left_rotate(node.parent)
            elif node.parent.left == node and node.parent.parent.left == node.parent:
                # Zig Zig Operation
                self.right_rotate(node.parent.parent)
                self.right_rotate(node.parent)
            elif node.parent.right == node and node.parent.parent.right == node.parent:
                # Zag Zag Operation
                self.left_rotate(node.parent.parent)
                self.left_rotate(node.parent)
            elif node.parent.right == node and node.parent.parent.left == node.parent:
                # Zag Zig Operation
                self.left_rotate(node.parent)
                self.right_rotate(node.parent)
            else:
                # Zig Zag Operation
                self.right_rotate(node.parent)
                self.left_rotate(node.parent)

    # Zig Operation
    def right_rotate(self, root):
        node = root.left
        root.left = node.right
        if node.right:
            node.right.parent = root
        
        node.parent = root.parent
        if root.parent is None:
            self.root = node
        elif root.parent.left == root:
            root.parent.left = node
        else:
            root.parent.right = node

        node.right = root
        root.parent = node

    # Zag Operation
    def left_rotate(self, root):
        node = root.right
        root.right = node.left
        if node.left:
            node.left.parent = root
        
        node.parent = root.parent
        if root.parent is None:
            self.root = node
        elif root.parent.right == root:
            root.parent.right = node
        else:
            root.parent.left = node

        node.left = root
        root.parent = node
        
    def search(self, value):
        def search_util(root, value):
            if root is None or root.data == value:
                return root
            if root.data > value:
                return search_util(root.left, value)
            else:
                return search_util(root.right, value)
        node = search_util(self.root, value)        
        if node is not None:
            self.splay(node)
            return node
        else:
            return None

    def insert(self, value):
        node = Node(value)
        parent = None
        root = self.root
        while root:
            parent = root
            if root.data >= value:
                root = root.left
            else:
                root = root.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif parent.data >= value:
            parent.left = node
        else:
            parent.right = node
        self.splay(node)

    def delete(self, value):
        node = self.search(value) 
        if node is None:
            return "Value Not Found in the Tree!"
        self.splay(node)
        
        # Splitting Operation
        if node.right:
            right_tree = node.right
            right_tree.parent = None
        else:
            right_tree = None        

        left_tree = node
        left_tree.right = None
        node = None
    
        # Joining Operation
        if left_tree.left:
            left_tree.left.parent = None
        
        self.root = self.join(left_tree.left, right_tree)
        left_tree = None

    def join(self, left_tree, right_tree):
        if left_tree is None: return right_tree
        if right_tree is None: return left_tree
        
        max_node = left_tree
        while max_node.right:
            max_node = max_node.right

        self.splay(max_node)
        max_node.right = right_tree
        right_tree.parent = max_node
        return max_node

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


if __name__ == "__main__":
    tree = SplayTree()
    print("==========================================")
    tree.insert(33)
    tree.insert(44)
    tree.insert(67)
    tree.insert(5)
    tree.insert(89)
    tree.insert(41)
    tree.insert(98)
    tree.insert(1)
    print_tree(tree.root)

    tree.search(33)
    tree.search(44)
    print("==========================================")
    print_tree(tree.root)

    tree.delete(89)
    tree.delete(67)
    tree.delete(41)
    tree.delete(5)
    print("==========================================")
    print_tree(tree.root)

    tree.delete(98)
    tree.delete(1)
    tree.delete(44)
    tree.delete(33)
    print("==========================================")
    print_tree(tree.root)






