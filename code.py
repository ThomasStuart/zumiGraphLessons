class Node:

    def __init__(self, n, p):
        self.name       = n
        self.position   = p
        self.visited    = False
        self.edges      = []

    def get_name(self):
        return self.name


    def get_edges(self):
        return self.edges
        
        
 class Edge:

    def __init__(self, startNode , endNode):
        self.startNode = startNode
        self.endNode   = endNode

    def get_startNode(self):
        return self.startNode

    def get_endNode(self):
        return self.endNode


    def get_startNode_name(self):
        return self.startNode.name


    def get_endNode_name(self):
        return self.endNode.name



from Node import Node
from Edge import Edge

class Graph:
    def __init__(self):
        self.nodes_dict = None
        self.edges_dict = None

    def create_simple(self):
        node_names = ['x', 'a', 's', 'b']
        node_pos = [(0, 10), (-10, 0), (0, 0), (10, 0)]
        nodes_dict = {}

        # Create nodes and add them to the dictionary
        for index in range(0, len(node_names)):
            key = node_names[index]
            value = Node(node_names[index], node_pos[index])
            nodes_dict[key] = value

        edges_dict = {}
        e1 = Edge(nodes_dict['s'], nodes_dict['x'])
        e2 = Edge(nodes_dict['a'], nodes_dict['s'])
        e3 = Edge(nodes_dict['b'], nodes_dict['s'])

        edges_dict['sx'] = e1
        edges_dict['as'] = e2
        edges_dict['bs'] = e3

        # add e1 to both vertices
        nodes_dict['s'].edges.append(e1)
        nodes_dict['x'].edges.append(e1)

        # add e2 to both vertices
        nodes_dict['a'].edges.append(e2)
        nodes_dict['s'].edges.append(e2)

        # add e3 to both vertices
        nodes_dict['b'].edges.append(e3)
        nodes_dict['s'].edges.append(e3)

        # set class vars
        self.nodes_dict = nodes_dict
        self.edges_dict = edges_dict


    def search(self, startChar, destinationChar):
        startNode = self.nodes_dict[startChar]
        destinationNode = self.nodes_dict[destinationChar]
        queue = []

        queue.append( ( startNode, [startNode]) )

        while (len(queue) > 0):
            currNode, currRoute = queue.pop(0)

            print("currNode:   ", currNode.get_name() )
            print("currRoute:  ", end="")
            for n in currRoute:
                print("->", n.get_name(), "<-", end="")
            print()
            currNode.visited = True

            if currNode == destinationNode:
                print("FOUND")
                return currRoute

            for edge in currNode.edges:
                print("Examining edge from ->", edge.get_startNode_name(), "<- to ->", edge.get_endNode_name(), "<-" )

                if   edge.startNode != currNode and edge.startNode.visited == False:
                    new_route = currRoute.copy()
                    new_route.append(  edge.startNode )
                    queue.append( ( edge.startNode, new_route   ) )
                elif edge.endNode != currNode and edge.endNode.visited == False:
                    new_route = currRoute.copy()
                    new_route.append(edge.endNode)
                    queue.append( ( edge.endNode,   new_route   ))

        return "FAILED"


 def main():
    G = Graph()
    G.create_simple()
    #G.create_complex()
    route = G.search('s', 'x')

    print("-----  Final Route: ----- " )
    i = 0
    for node in route:
        print("\t Node(",i, ")->", node.get_name() , "<-")
        i+=1

if __name__ == "__main__":
    main()

