class Graph(object):
    '''
        https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
    '''
    def __init__(self, graph_dict = None):
        self.graph_dict = graph_dict

    def add_vertex(self, vertex):
        # Since graph is represented by a Dictionary. 
        # This method will simply add the vertex if it doesn't exist else do nothing.
        # This is to avoid KeyError.        
        try:
            key = self.graph_dict[vertex]
        except KeyError:
            self.graph_dict[vertex] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        # This will add 1 directional edge. Call this method twice in order to add a 2-way Edge.
        self.graph_dict[v1].append(v2)
        
    def generate_edges(self):
        result = []
        for vertex in self.graph_dict:
            for neighbor in self.graph_dict[vertex]:
                result.append((vertex, neighbor))        
        return str(result)

    def __repr__(self):
        result = '{\n'
        for vertex in self.graph_dict:
            result = result + vertex + ": "
            result = result + str(self.graph_dict[vertex]) + "\n"
        result += '}'
        return result

    def find_any_possible_path(self, start, end, path = []):
        path.append(start)
        if start == end:
            return path
        for v in self.graph_dict[start]:
            if v not in path:
                new_path = self.find_any_possible_path(v, end, path)
                if new_path:
                    return new_path
                else:
                    return None

    def dfs_recursion_complete(self):
        # This method will do a complete Depth First Search by using Recursion.
        # It will also cover the disconnected Points.
        visit_status = {}
        for v in self.graph_dict:
            visit_status[v] = False
        for v in self.graph_dict:
            if not visit_status[v]:
                self.dfs_dict(v, visit_status)
        print()

    def dfs_recursion(self, vertex):
        # This method will just do a DFS search starting with given vertex.
        # It will not be able to cover the disconnected points.
        visit_status = {}
        for v in self.graph_dict:
            visit_status[v] = False
        self.dfs_dict(vertex, visit_status)
        print()

    def dfs_dict(self, vertex, visit_status):
        visit_status[vertex] = True
        print(vertex, end = ' ')
        for i in self.graph_dict[vertex]:
            if not visit_status[i]:
                self.dfs_dict(i, visit_status)

    def bfs_iter(self, vertex):
        # This method will do the Breadth First Search by using a Queue. It will not cover disconnected points.
        visit_status = {}
        for v in self.graph_dict:
            visit_status[v] = False
        queue = []
        queue.append(vertex)
        visit_status[vertex] = True        
        while len(queue) > 0:
            v = queue.pop(0)
            print(v, end = ' ')
            for i in self.graph_dict[v]:
                if not visit_status[i]:
                    queue.append(i)
                    visit_status[i] = True
        print()

    def dfs_iter_complete(self):
        # This method will do a complete DFS search by using Stack mean it will cover the disconnected points as well.
        # Similar method can be created for a complete BFS as well.
        visit_status = {}
        for v in self.graph_dict:
            visit_status[v] = False
        for v in self.graph_dict:
            if not visit_status[v]:
                self.dfs_iter_util(v, visit_status)
        print()

    def dfs_iter_util(self, vertex, visit_status):
        stack = []
        stack.append(vertex)
        visit_status[vertex] = True
        while len(stack) > 0:
            v = stack.pop()
            print(v, end = ' ')
            for i in self.graph_dict[v]:
                if not visit_status[i]:
                    stack.append(i)
                    visit_status[i] = True

    def dfs_iter(self, vertex):
        # This method will do the Depth First Search by using a Stack. It wont cover disconnected points.
        # Use the reversed method inside the for loop of popped vertex in order to match the output with recusrion method.
        # If reversed is not used then output will be different but both will be a valid Depth First Search.
        visit_status = {}
        for v in self.graph_dict:
            visit_status[v] = False
        stack = []
        stack.append(vertex)
        visit_status[vertex] = True
        
        while len(stack) > 0:
            v = stack.pop()
            print(v, end = ' ')            
            for i in self.graph_dict[v]:
                if not visit_status[i]:
                    stack.append(i)
                    visit_status[i] = True
        print()

    def get_first_possible_path(self, start, end):
        # This method will return the first possible path between given vertex.
        # If no path exists between the two then it will return.
        visit_status = {}
        for v in graph.graph_dict:
            visit_status[v] = False
        queue = []
        path = []
        queue.append(start)
        visit_status[start] = True
        while len(queue) > 0:
            v = queue.pop(0)
            path.append(v)
            if v == end:
                return path
            for i in self.graph_dict[v]:
                if not visit_status[i]:
                    queue.append(i)
                    visit_status[i] = True
        return None     

    def get_all_paths(self, start, end):
        # Algorithm:
        # Create list path for tracking visited nodes in current path.
        # Create list paths for tracking found paths.
        # Create dictionary visit_status to track the visited status.
        # Call util methods for start and end nodes.
        visit_status = {}
        for v in self.graph_dict:
            visit_status[v] = False        
        paths = []
        path = []
        self.get_all_paths_util(start, end, visit_status, path, paths)
        return paths
    
    def get_all_paths_util(self, start, end, visit_status, path, paths):
        # Algorithm:
        # mark visit status of start node as True.
        # Append start node in path list.
        # Check if start = end then add the path list in paths.
        # take out the start node from the path and update its visit status to False so that other paths can use this node.
        # if start != end then call this method for all neibhors of start with visit status as False.
        visit_status[start] = True
        path.append(start)
        if start == end:
            paths.append(list(path))
        else:
            for i in self.graph_dict[start]:
                if not visit_status[i]:
                    self.get_all_paths_util(i, end, visit_status, path, paths)
        node = path.pop()
        visit_status[start] = False     

    def get_shortest_path(self, start, end):
        # Algorithm: Exactly similar to find all paths except here we will compare the length before updating the result.
        visit_status = {}
        for v in self.graph_dict:
            visit_status[v] = False
        path = []
        result = []
        self.get_shortest_path_util(start, end, visit_status, path, result)
        if len(result) > 0: 
            return result[0]
        else: 
            return None

    def get_shortest_path_util(self, start, end, visit_status, path, result):
        visit_status[start] = True
        path.append(start)
        if start == end:
            if len(result) == 0:
                result.append(list(path))
            elif len(path) < len(result[0]):
                result[0] = list(path)
            # result.append(list(path))
        else:
            for r in self.graph_dict[start]:
                if not visit_status[r]:
                    self.get_shortest_path_util(r, end, visit_status, path, result)
        path.pop()
        visit_status[start] = False

if __name__ == "__main__":
    d = {
        'a': ['c'],
        'b': ['d'],
        'c': ['e', 'a'],
        'd': ['a', 'd'],
        'e': ['b', 'c'],
        'f': []
    }

    graph = Graph(d)
    # print(graph.generate_edges())
    print(graph)
    # print(graph.find_any_possible_path('a', 'e', []))
    # print(graph.find_an
    # y_possible_path('b', 'e', []))    
    # graph.dfs_recursion('e')
    # graph.dfs_recursion_complete()
    # graph.bfs_iter('e')
    # graph.dfs_iter('e')
    # graph.dfs_iter_complete()
    # print(graph.get_first_possible_path('a', 'b'))
    # print(graph.get_first_possible_path('c', 'a'))    
    print(graph.get_all_paths('c', 'a'))
    print(graph.get_shortest_path('c', 'a'))