from DirectedDegrees import getVertexPairs

def degrees(vertexPairs:list[list[str]]):
    degrees = {}
    for pair in vertexPairs:
        for vertex in pair:
            degrees[vertex] = degrees.get(vertex,0) + 1
    return degrees

if __name__ == "__main__":
    vertexPairs = getVertexPairs()
    vertexDegrees = degrees(vertexPairs)
    for vertex,degree in vertexDegrees.items():
        print(f"{degree} is the degree of vertex {vertex}")