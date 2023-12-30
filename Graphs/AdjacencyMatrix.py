from isBipartite import createAdjacencyList
from DirectedDegrees import getVertexPairs

def adjacencyMatrix(vertexPairs):
    adjacencyList  = createAdjacencyList(vertexPairs, isDirected=True)
    # Create a set of all vertices
    vertices = list(adjacencyList.keys())
    vertices.sort()
    # Create a dictionary to map vertices to indices
    vertex_to_index = {vertex: index for index, vertex in enumerate(vertices)}
    # Initialize an empty matrix
    matrix = [[0 for _ in vertices] for _ in vertices]
    # Fill the matrix
    for vertex, neighbors in adjacencyList.items():
        for neighbor in neighbors:
            index1 = vertex_to_index[vertex]
            index2 = vertex_to_index[neighbor]
            matrix[index1][index2] += 1 
    return matrix

if __name__ == "__main__":
    vertexPairs = getVertexPairs()
    matrix = adjacencyMatrix(vertexPairs)
    print("The adjacency matrix is:")
    for row in matrix:
        print(row)