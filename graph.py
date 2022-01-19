class graph:
    def __init__(self, max_graph_size):
        """

        :param max_graph_size: maximum size of the graph
        """
        self.max_graph_size = max_graph_size
        self.nodes = set(())
        self.edges = set(())
        self.visited_nodes = []
        self.adj_list = []
        for i in range(self.max_graph_size):
            node = i + 1
            self.nodes.add(node)
            if len(self.nodes) == self.max_graph_size:
                print("set of nodes: ")
                print(self.nodes)

    def add_edge(self, u, v):
        """
        adds an edge between two given variables, u and v, the edge will be a tuple

        :param u:  start of edge
        :param v:  end of edge
        :return:   True if an edge could be made (u and v must be in nodes), false if not
        """
        if u in self.nodes:  # an edge can only be made between two nodes
            if v in self.nodes:
                edge = (u, v)   # an edge should be a tuple
                self.edges.add(edge)  # add the edge to the set
                print(self.edges)
                print(f"node {u} is adjacent to node {v}")
                return True
        else:
            return False

    def check_adjacent(self, node):
        """
        checks to see the edges between the node you use as the param and all the nodes its connected to
        :param node:  the node that you want to check what it is adjacent to
        :return: list of adjacent nodes
        """
        for item in self.edges:
            if node in item:
                self.adj_list.append(item)
        return self.adj_list

    def breadth_traversal(self, starting_node):
        """
        starts at given node.
        appends node to list, adds to visited_nodes
        looks for edges that link this node to others.
        checks to see if nodes are unvisited.
        if it is:
            traverse edge, appends visited node to list, adds node to visited_nodes
        repeat

        :param starting_node: the node that you want to start at. has to be in self.nodes
        :return:
        """
        traversal_list = [starting_node]
        current_pos = 0
        traversing = True
        for node in traversal_list:
            self.check_adjacent(node)
        while traversing:
            for edge in self.adj_list:
                adj_node = sum(edge) - int(traversal_list[current_pos])
                if adj_node not in self.visited_nodes:
                    traversal_list.append(adj_node)
                    print(traversal_list)
                current_pos += 1
                for node in traversal_list:
                    self.visited_nodes.append(node)



    def depth_traversal(self):
        pass


graph = graph(10)
