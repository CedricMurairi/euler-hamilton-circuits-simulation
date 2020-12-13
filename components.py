import random
   
# This class represents a undirected graph using adjacency list representation

symbs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
p_symb = []

class Graph: 
   
    def __init__(self, vertices):
        self.V = vertices # No. of vertices 
        self.graph = [] # default list to store verteces
        self.visited_verteces = []
   
    # function to add an edges to graph 
    def addEdge(self):
        for _ in range(self.V):
            self.graph.append(Vertex(random.uniform(0, width), random.uniform(0, height), 8))
        for vert in self.graph:
            for _ in range(random.randint(1, 2)):
                if len(vert.others) == 2:
                    break
                vert.others.append(self.get_random_v(vert))
                
    def get_random_v(self, vert):
        rand_v = random.choice(self.graph)
        if rand_v == vert:
            return self.get_random_v(vert)
        return rand_v
   
    '''Method to check if all non-zero degree vertices are 
    connected. It mainly does DFS traversal starting from  
    node with non-zero degree'''
    
    def isConnected(self):
        connected = 0
        for vert in self.graph:
            if len(vert.linked) > 0:
                connected += 1
        if connected == self.V:
            return True
        return False
  
    '''The function returns one of the following values
       0 --> If grpah is not Eulerian 
       1 --> If graph has an Euler path (Semi-Eulerian) 
       2 --> If graph has an Euler Circuit (Eulerian)'''
       
    def isEulerian(self):
        # Check if all non-zero degree vertices are connected
        print('Connected: ' + str(self.isConnected()))
        if not self.isConnected():
            print('The Graph is not connected!')
            return False
        else: 
            # Count vertices with odd degree 
            odd = 0
            for vert in self.graph: 
                if len(vert.linked) % 2 != 0:
                    odd += 1
            print('Odd degree verteces: {}'.format(odd))
  
            '''If odd count is 2, then semi-eulerian. 
            If odd count is 0, then eulerian 
            If count is more than 2, then graph is not Eulerian 
            Note that odd count can never be 1 for undirected graph'''
            
            if odd == 0: 
                return 2
            elif odd == 2: 
                return 1
            elif odd > 2: 
                return 0
            
    def isHamiltonian(self):
        vert_x = 0
        if not self.isConnected():
            return False
        else:
            for vert in self.graph:
                if len(vert.linked) >= self.V / 2:
                    vert_x += 1
            if vert == self.V:
                return 1
            else:
                return 0
  
  
    # Function to run test cases 
    def testEulerian(self):
        for vert in self.graph:
            print('{} connects to {}'.format(vert.sym.upper(), [other.sym.upper() for other in vert.others]))
        res = self.isEulerian() 
        if res == 0: 
            print "Graph is not Eulerian"
        elif res ==1 : 
            print "Graph has a Euler path"
        elif res == 2: 
            print "Graph has a Euler cycle | circuit"
        else:
            print "Strange thing"
            
    def testHamilton(self):
        res = self.isHamiltonian()
        if res == 1:
            print "Graph has Hamiltonian cycle"
        else:
            print "Graph has no Hamiltonian cycle"

class Vertex:
    def __init__(self, x, y, rad=10):
        self.x = x
        self.y = y
        self.rad = rad
        self.sym = self.get_sym()
        self.others = []
        self.linked = []
    
    def get_sym(self):
        global symbs
        sym = random.choice(symbs)
        if sym in p_symb:
            return self.get_sym()
        p_symb.append(sym)
        return sym
        
    def show(self):
        font = loadFont("Monospaced.bold-48.vlw")
        textFont(font, 10)
        fill(0)
        text(self.sym, self.x + 1, self.y + 1)
        fill(0)
        circle(self.x, self.y, self.rad)
        
    def link(self):
        for vert in self.others:
            if vert not in self.linked:
                fill(0)
                line(self.x, self.y, vert.x, vert.y)
                self.linked.append(vert)
                vert.linked.append(self)
