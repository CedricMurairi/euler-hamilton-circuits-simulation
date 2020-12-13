import random
from components import Vertex, Graph

RAD = 10
graph = None
verteces = []

def setup():
    global verteces
    global graph
    size(500, 500)
    graph = Graph(10)
    graph.addEdge()
    
def draw():
    global verteces
    global graph
    # print(graph.graph)
    background(255)
    for vert in graph.graph:
        vert.show()
    for vert in graph.graph:
        vert.link()
        # vert.move()
    graph.testEulerian()
    graph.testHamilton()
    
    # font = loadFont("Monospaced.bold-48")
    # background(0)
    # textFont(font)
    # text("word", 12, 60)
    
    # font = loadFont("Monospaced.bold-48.vlw")
    # textFont(font, 32)
    # fill(255)
    # text("word", 10, 50)
    
    noLoop()

def keyPressed():
    if keyCode == 'b' or keyCode == 'B':
        print('Hello, key B or b pressed success')
    
        
def mouseReleased():
    for vert in verteces:
        distance = dist(mouseX, mouseY, vert.x, vert.y)
        if distance <= vert.rad:
            print('You are within the Circle, launching to Mars!')
