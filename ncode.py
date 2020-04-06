class Node: 
    def __init__(self, name, edges, position, visited ):
        self.name       = name 
        self.edges      = edges 
        self.position   = position 
        self.visited    = visited
    
    def getName(self):
        return self.name
    
    def getEdges(self):
        return self.edges
        
    def getPosition(self):
        return self.position 
    
    def getVisited(self):
        return self.visited


class Edge: 
    def __init__(self, name, node1,node2):
        self.name      = name 
        self.startNode = node1
        self.endNode   = node2
        
    def getName(self):
        return self.name


class Graph:
    
    def __init__(self):
        # dict means it's a dictionary
        self.nodes_dict = {}
        self.edges_dict = {}

    def create_simple_graph(self):
        
        # we defined our nodes  
        nodeA = Node('A', [], (-10,0) , False)
        nodeS = Node('S', [], (0,0)   , False)
        nodeB = Node('B', [], (10,0)  , False)
        nodeX = Node('X', [], (0,10)  , False)
        
        # we defined the edges
        e1 = Edge( "e1", nodeX, nodeS )
        e2 = Edge( "e2", nodeA, nodeS )
        e3 = Edge( "e3", nodeS, nodeB )
        

        # add the edges to the their respected nodes
        nodeS.edges.append( e1 )
        nodeS.edges.append( e2 )
        nodeS.edges.append( e3 )
        nodeA.edges.append( e2 )
        nodeB.edges.append( e3 )
        nodeX.edges.append( e1 )
        
        
        self.nodes_dict['A'] = nodeA
        self.nodes_dict['B'] = nodeB
        self.nodes_dict['S'] = nodeS
        self.nodes_dict['X'] = nodeX
        
        self.edges_dict['e1'] = e1
        self.edges_dict['e2'] = e2
        self.edges_dict['e3'] = e3
        
    def getNodesDict(self):
        return self.nodes_dict
        

G = Graph()
G.create_simple_graph() 
nd = G.getNodesDict()

print( nd['A'].name , ':', nd['A'].position )
listA = nd['A'].getEdges()
for edge in listA:
    print( edge.getName() ) 
    
print()
print()


print( nd['B'].name , ':', nd['B'].position )
listB = nd['B'].getEdges()
for edge in listB:
    print( edge.getName() ) 
print()
print()

print( nd['S'].name , ':', nd['S'].position )
listS = nd['S'].getEdges()
for edge in listS:
    print( edge.getName() ) 
    
print()
print()

print( nd['X'].name , ':', nd['X'].position )
listX = nd['X'].getEdges()
for edge in listX:
    print( edge.getName() ) 
