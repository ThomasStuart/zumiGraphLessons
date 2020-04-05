
class Node: 
    def __init__(self, n, es , pos , vis):
        self.name = n
        self.edges = es   # because its a list
        self.position = pos
        self.visited = vis
        
    def getName(self):
        return self.name
    
    def getEdges(self):
        return self.edges 
    
    def getPosition(self):
        return self.position 
    
    def getVisited(self):
        return self.visited 

# write it from scratch
class Edge: 
    def __init__(self, n1,n2):
        self.startNode = n1
        self.endNode   = n2
        
    # getter startNode
    def getStartNode(self):
        return startNode
    
    # getter endNode
    def getStartNode(self):
        return endNode

class Graph:
    
    def __init__(self):
        self.node_dict = {}
        self.edge_dict = {}
        
    def simple_graph(self):
        
        #Exercise:  create the 4 nodes (A,S,B,X):
        nodeS = Node('S', [],   (0,0), False)
        nodeA = Node('A', [], (-10,0), False)
        nodeB = Node('B', [],  (10,0), False)
        nodeX = Node('X', [],  (0,10), False)
        
    
        # create the edges 
        e1 = Edge(nodeS, nodeX)
        e2 = Edge(nodeA, nodeS)
        e3 = Edge(nodeS, nodeB)
        
        self.edge_dict['e1']  = e1 
        self.edge_dict['e2']  = e2 
        self.edge_dict['e3']  = e3 
        
        
        #add the individual edges to their respected nodes
        nodeS.edges.append( e1 )
        nodeS.edges.append( e2 )
        nodeS.edges.append( e3 )
        
        #jason for node a
        nodeA.edges.append( e2 )
        
        # richardson for node b 
        nodeB.edges.append( e3 )
        
        #node X
        nodeX.edges.append( e1 )
        
        
        self.node_dict['A'] = nodeA
        self.node_dict['B'] = nodeB
        self.node_dict['S'] = nodeS
        self.node_dict['X'] = nodeX
        
        
    def print_nodes(self):
        #print the nodes by using the dictionary
        # hint: use a for loop
        
        for node in self.node_dict.values():
            # 1. print the name of the node  using the getter fx 
            print(  node.getName() , end='' )
            # 2. print the postion of the node using the getter fx
            print(   node.getPosition()  )
            
            #print(  node.getEdges()  ) 
            
def foo():
    print("Hey")
        

#  Exercise: 
# 1. create a Graph object called 'G'
G = Graph()

# it can call the simple_graph now 
# 2. call the simple_graph function on the object'G'
#    to create the actual graph G* 
G.simple_graph()


# Jason: tell me the code 
G.print_nodes() 

