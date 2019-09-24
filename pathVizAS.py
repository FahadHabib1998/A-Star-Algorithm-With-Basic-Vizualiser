import sys
import matplotlib.pyplot as plt

#Class to make a node for each coordinate
class Node():
    def __init__(self,parent = None, position = None):
        
        self.parent = parent
        self.position = position
        #Distance between current node and the start node
        self.g = 0
        #Distance from current node to the end node
        self.h = 0
        # g+f
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def aStar(maze, start, end):

    startNode = Node(None,start)
    startNode.g = startNode.h = startNode.f = 0

    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0
    #Collection of all generated nodes
    openList = []
    #Collection of all expanded/explored node 
    closeList = []

    openList.append(startNode)
    
    while len(openList) > 0:
        #Current Node
        crntNode = openList[0]
        crntIndex = 0
        #loop to find node with smallest 'f'
        for index, node in enumerate(openList):
            if node.f < crntNode.f:
                crntNode = node
                crntIndex = index
                
        openList.pop(crntIndex)
        closeList.append(crntNode)
        #If end node reached 
        if(crntNode == endNode):
            path = []
            curr = crntNode
            while curr is not None:
                path.append(curr.position)
                curr = curr.parent
            return path[::-1]
        #Generating childrens(Adjacent nodes)
        children = []
        childCoord = [(0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,-1),(1,1),(-1,-1)]

        for coord in childCoord:
            childPos = (crntNode.position[0]+coord[0], crntNode.position[1]+coord[1])
            
            if childPos[0] > (len(maze)-1) or childPos[0] < 0 or childPos[1] > (len(maze[len(maze)-1]) -1) or childPos[1] < 0:
                continue
            if maze[childPos[0]][childPos[1]] != 0:
                continue
            
            childNode = Node(crntNode, childPos)
            children.append(childNode)

            for child in children:
                for closed in closeList:
                    if child == closed:
                        continue
                child.g = crntNode.g + 1
                child.h = ((child.position[0] - endNode.position[0])**2) + ((child.position[1] - endNode.position[1])**2)
                child.f = child.g + child.h

                for opened in openList:
                    if opened == child:
                        continue
                openList.append(child)

    
                
    


maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

start = (1, 1)
end = (11, 10)
path = aStar(maze, start, end)
for i in path:
    maze[i[0]][i[1]] = 2
plt.imshow(maze)
plt.show()

    
