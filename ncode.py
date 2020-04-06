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
        
        
        nodes_dict['A'] = nodeA
        nodes_dict['B'] = nodeB
        nodes_dict['S'] = nodeS
        nodes_dict['X'] = nodeX
        
        edges_dict['e1'] = e1
        edges_dict['e2'] = e2
        edges_dict['e3'] = e3
        
def foo():
    print( "hello")
        
# Exercise: 
#foo()
create_simple_graph()

        
