from zumi.zumi import Zumi

zumi = Zumi()
zumi.mpu.calibrate_MPU()

# CONSTANTS
DIV_CONST = 6.0
POWER = 40
# variables 
heading = 0


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

    def __init__(self, eName, startNode , endNode, alpha, beta):
        self.edgeName = eName
        self.startNode = startNode
        self.endNode   = endNode
        self.startNodeDirToEndNode = alpha
        self.endNodeDirToStartNode = beta

    def get_edgeName(self):
        return self.edgeName

    def get_startNode(self):
        return self.startNode

    def get_endNode(self):
        return self.endNode


    def get_startNode_name(self):
        return self.startNode.name

    def get_endNode_name(self):
        return self.endNode.name

    def get_startNodeDirToEndNode(self):
        return self.startNodeDirToEndNode

    def get_endNodeDirToStartNode(self):
        return self.endNodeDirToStartNode


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
        e1 = Edge( "e1", nodes_dict['s'], nodes_dict['x'], 90, 270)
        e2 = Edge( "e2", nodes_dict['a'], nodes_dict['s'], 0, 180)
        e3 = Edge( "e3", nodes_dict['b'], nodes_dict['s'], 180, 0)

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
        startNode       = self.nodes_dict[startChar]
        destinationNode = self.nodes_dict[destinationChar]
        queue = []
        queue.append( ( startNode, []) )

        while (  len(queue) > 0  ):

            currNode, currRoute = queue.pop(0)

            # print("currNode:   ", currNode.get_name() )
            # print("currRoute:  ", end="")
            # for n in currRoute:
            #     print("->", n.get_name(), "<-", end="")
            # print()
            currNode.visited = True

            if currNode == destinationNode:
                print("FOUND")
                return currRoute

            for edge in currNode.edges:
                #print("Examining edge from ->", edge.get_startNode_name(), "<- to ->", edge.get_endNode_name(), "<-" )
                if   edge.startNode != currNode and edge.startNode.visited == False:
                    new_route = currRoute.copy()
                    new_route.append( ( edge, edge.get_endNodeDirToStartNode() ))
                    #new_route.append(  edge.startNode )
                    queue.append( ( edge.startNode, new_route   ) )
                elif edge.endNode != currNode and edge.endNode.visited == False:
                    new_route = currRoute.copy()
                    new_route.append( ( edge, edge.get_startNodeDirToEndNode() ))
                    #new_route.append(edge.endNode)
                    queue.append( ( edge.endNode,   new_route   ))

        return "FAILED"


def getTimeForTravel(distanceInInches):
    time = (distanceInInches + 1) / DIV_CONST
    return time

def change_heading_to_desired_heading( currHeading, desiredHeading):
        # step1: calc the magnitude of angle change , call it X
        X = desiredHeading - currHeading
        print("X", X)
        zumi.turn(X)
        return desiredHeading
    
def main():
    G = Graph()
    G.create_simple()
    #G.create_d_graph()
    #G.create_complex()
    route = G.search('s', 'x')
    #route = G.search('s', 'a')
    #route = G.search('s', 'b')


    print("-----  Final Route: ----- " )
    i = 0
    for item in route:
        print("\t edge name: ", item[0].get_edgeName(), "desired angle", item[1] ) 
        i+=1
    
    
#     while len( route ) != 0 :
#         pair = route[0]  # pair = (90, 10)

#         desired_angle    = pair[0]  # 90
#         desired_distance = pair[1]  # 10

#         # Step1: change heading to desired heading 
#         change_heading_to_desired_heading( heading, desired_angle )


#         # Step2: get the distance we need to go 
#         time = getTimeForTravel(desired_distance)
#         zumi.forward(POWER, time)


#         # Step3: deletes the first element in list
#         route.pop(0)




if __name__ == "__main__":
    main()
