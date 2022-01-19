class graph:
    def __init__(self, max_graph_size):
        """

        :param max_graph_size: maximum size of the graph
        """
        self.max_graph_size = max_graph_size
        self.nodes = set(())
        self.edges = set(())
        self.visited_nodes = []
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
        if u and v in self.nodes:  # an edge can only be made between two nodes
            edge = (u, v)   # an edge should be a tuple
            self.edges.add(edge)  # add the edge to the set
            print(self.edges)
            print(f"node {u} is adjacent to node {v}")
            return True
        else:
            return False
    def check_adjacent(self):
        for item in self.edges:
            print(item)
    def breadth_traversal(self, starting_node):
        """
        starts at given node.
        appends node to list, removes node from unvisited_nodes
        looks for edges that link this node to others.
        checks to see if nodes are unvisited.
        if it is:
            traverse edge, appends visited node to list, removes node from unvisited_nodes
        repeat

        :param starting_node: the node that you want to start at. has to be in self.nodes
        :return:
        """


    def depth_traversal(self):
        pass


graph = graph(10)
