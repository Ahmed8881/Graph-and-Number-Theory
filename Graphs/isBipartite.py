from DirectedDegrees import getVertexPairs

def createAdjacencyList(vertexPairs, isDirected=False):
    """
    This function takes in a list of vertex pairs and returns an adjacency list for a graph
    """
    adjacencyList = {}
    for edge in vertexPairs:
        vertex1,vertex2 = edge
        if vertex1 in adjacencyList:
            adjacencyList[vertex1].append(vertex2)
        else:
            adjacencyList[vertex1] = [vertex2]
        if not isDirected:      # If the graph is undirected, add the reverse edge
            if vertex2 in adjacencyList:
                adjacencyList[vertex2].append(vertex1)
            else:
                adjacencyList[vertex2] = [vertex1]
    return adjacencyList

def isBipartite(vertexPairs):
    """
    This function takes in a list of vertex pairs and returns True if the graph is bipartite and False otherwise
    It works by assigning a color to each vertex and then checking if the neighbors of the vertex have the opposite color
    """
    # Create an adjacency list from the vertex pairs
    adjacencyList = createAdjacencyList(vertexPairs)
    # Create a dictionary to store the colors of the vertices
    colors = {}
    # Loop through the vertices in the adjacency list
    for vertex in adjacencyList:
        # If the vertex has not been assigned a color, assign it a color and add it to the queue
        if vertex not in colors:
            colors[vertex] = 0
            queue = [vertex]
            while queue:
                # pop current element from the queue
                currentVertex = queue.pop(0)
                # loop over the neighbors of the current vertex
                for neighbor in adjacencyList[currentVertex]:
                    if neighbor not in colors:
                        # Assign opposite color to the neighbor
                        colors[neighbor] = 1 - colors[currentVertex]
                        # Add it to the queue so that its neighbors can be colored
                        queue.append(neighbor)
                        # If the neighbor has already been colored and it has the same color as the current vertex, the graph is not bipartite
                    elif colors[neighbor] == colors[currentVertex]:
                        return False
    return True

if __name__ == "__main__":
    vertexPairs = getVertexPairs()
    if isBipartite(vertexPairs):
        print("The graph is bipartite")
    else:
        print("The graph is not bipartite")