def getVertexPairs():
    totalEdges = int(input("Enter the number of edges: "))
    vertexPairs = [input(f"Enter the vertex pair for edge {i+1} (seperated by a comma ','): ").split(',') for i in range(totalEdges)]
    return vertexPairs


def degrees(vertexPairs:list[list[str]]):
    degrees = {}
    for pair in vertexPairs:
        initialVertex, terminalVertex = pair
        degrees[initialVertex+'(out)'] = degrees.get(initialVertex+"(out)",0)+1
        degrees[terminalVertex+'(in)'] = degrees.get(terminalVertex+"(in)",0)+1
    return degrees


if __name__ == "__main__":
    vertexPairs = getVertexPairs()
    vertexDegrees = degrees(vertexPairs)
    for vertex,degree in vertexDegrees.items():
        vertexName = vertex[:vertex.find('(')]
        degreeType = "in-degree" if vertex[vertex.find('(')+1:-1] == "in" else "out-degree"
        print(f"{degree} is the {degreeType} of vertex {vertexName}")