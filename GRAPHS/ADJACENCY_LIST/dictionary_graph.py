class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def add_in_start(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, self.head)
    def add_in_end(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node
    def remove_head(self):
        data = self.head.data
        if self.head == self.tail:            
            self.head = self.tail = None
        else:
            self.head = self.head.next
        return data
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    def __repr__(self):
        result = []
        node = self.head
        while node:
            result.append(str(node.data))
            node = node.next
        return ' -> '.join(result)

class Graph(object):
    '''
        https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
    '''
    def __init__(self):
        self.data = {}
    
    def add_node(self, node):
        try:
            value = self.data[node]
        except:
            self.data[node] = []
    
    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.data[node1].append(node2)
        self.data[node2].append(node1)
    
    def generate_edges(self):
        for node in self.data:
            for nbhr in self.data[node]:
                print(f'{node} -> {nbhr}')
    
    def __repr__(self):
        result = '{\n'
        for node in self.data:
            result = result + node + ': ' + ', '.join([str(x) for x in self.data[node]]) + '\n' 
        result += '}'
        return result

    def dfs_complete(self):
        '''
            This algorithm will do a Complete Depth First Search of the Graph that is it will include the Disconnected 
            Nodes as well. It will use a Stack to implement it.
            If we just need to do a DFS from a Node then implement the Util method by passing the starting Node.
        '''
        def dfs_util(node, visit_status):
            stack = LinkedList()
            stack.add_in_start(node)
            visit_status[node] = True
            while len(stack) > 0:
                node = stack.remove_head()
                print(node, end=' ')

                for nbhr in self.data[node]:
                    if not visit_status[nbhr]:
                        stack.add_in_start(nbhr) 
                        visit_status[nbhr] = True
        
        visit_status = {}
        for node in self.data:
            visit_status[node] = False
        for node in self.data:
            if not visit_status[node]:
                dfs_util(node, visit_status)

    def bfs_complete(self):
        '''
            This algorithm will do a Complete Breadth First Search of the Graph that is it will include the Disconnected 
            Nodes as well. It will use a Queue to implement it.
            If we just need to do a BFS from a Node then implement the Util method by passing the starting Node.
        '''
        def bfs_util(node, visit_status):
            queue = LinkedList()
            queue.add_in_end(node)
            visit_status[node] = True
            while len(queue) > 0:
                node = queue.remove_head()
                print(node, end=' ')
                for nbhr in self.data[node]:
                    if not visit_status[nbhr]:
                        queue.add_in_end(nbhr)
                        visit_status[nbhr] = True 
        
        visit_status = {}
        for node in self.data:
            visit_status[node] = False
        for node in self.data:
            if not visit_status[node]:
                bfs_util(node, visit_status)                

    def get_any_path(self, start, end):
        '''
            We will do a BFS on the Graph starting from the Start Node. If we get the End node during Traversal
            then Path will be returned.
            If Traversal Loop is completed then we will return "Path Not Found"
        '''
        def get_any_path_util(node, end, visit_status):
            result = []
            queue = LinkedList()
            queue.add_in_end(start)
            visit_status[start] = True
            
            while len(queue) > 0:
                node = queue.remove_head()
                result.append(node)
                if node == end:
                    return ' -> '.join(result)
                for nbhr in self.data[node]:
                    if not visit_status[nbhr]:
                        queue.add_in_end(nbhr)
                        visit_status[nbhr] = True
            return 'Path Not Found'

        visit_status = {}
        for node in self.data:
            visit_status[node] = False
        return get_any_path_util(start, end, visit_status)

    def get_all_paths(self, start, end):
        '''   
            This algorithm uses a slight tweak in normal Graph Traversal.
            Declare 2 lists: path and paths.
            Call a util method with start, end, visit_status, path and paths.
            Now, once we are done with processing util for a start node, pop the start node (or the last node) from path and
            set its visit_status to False so this node can be found by other possible paths as well.
        '''
        def get_all_paths_util(start, end, visit_status, path, paths):
            path.append(start)
            visit_status[start] = True

            if start == end:
                paths.append(list(path))
            else:
                for nbhr in self.data[start]:
                    if not visit_status[nbhr]:
                        get_all_paths_util(nbhr, end, visit_status, path, paths)
            node = path.pop()
            visit_status[start] = False

        visit_status = {}
        path = []
        paths = []
        for node in self.data:
            visit_status[node] = False
        get_all_paths_util(start, end, visit_status, path, paths)
        return paths

    def get_shortest_path(self, start, end):
        '''
            Get the complete list of paths and choose the shortest length one.
        '''
        paths = self.get_all_paths(start, end)     
        if len(paths) > 0:
            result = sorted(paths, key = lambda x: len(x))
            return result[0]
        else:
            return "Path Not Found"

if __name__ == "__main__":
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'c')
    g.add_edge('c', 'd')
    g.add_edge('c', 'e')
    g.add_edge('d', 'e')
    g.add_node('f')

    print(g)
    g.generate_edges()

    g.dfs_complete()
    print()
    g.bfs_complete()
    print()

    print(g.get_any_path('d', 'f'))
    print(g.get_all_paths('a', 'e'))

    print('===========')
    print(g.get_shortest_path('a', 'e'))


