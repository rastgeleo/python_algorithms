"""
Vertex stores some data.
Vertex stores the edges to connected vertices and their weight.
Vertex can add a new edge to its collection.
Graph stores all the vertices.
Graph knows if it is directed or undirected.
Graph can add a new vertex to its collection.
Graph can add a new edge between stored vertices.
Graph can tell whether a path exists between stored vertices.
"""


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())


class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(
                from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        visited = []    # Track visited vertices

        while len(start) > 0:
            current_vertex = start.pop(0)
            if current_vertex not in visited:
                visited.append(current_vertex)

            print("Visiting " + current_vertex)
            if current_vertex == end_vertex:
                print('path found!')
                return True
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()

                next_vertices = set(next_vertices) - set(visited)
                # add only vertices that has not been vistited
                start.extend(next_vertices)

        print('path not found.')
        return False


if __name__ == '__main__':

    railway = Graph()

    callan = Vertex('callan')
    peel = Vertex('peel')
    ulfstead = Vertex('ulfstead')
    harwick = Vertex('harwick')
    oxted = Vertex('oxted')
    godstone = Vertex('godstone')

    railway.add_vertex(callan)
    railway.add_vertex(peel)
    railway.add_vertex(harwick)
    railway.add_vertex(ulfstead)
    railway.add_vertex(oxted)
    railway.add_vertex(godstone)

    railway.add_edge(peel, harwick)
    railway.add_edge(harwick, callan)
    railway.add_edge(harwick, oxted)
    railway.add_edge(callan, peel)
    railway.add_edge(callan, godstone)

    peel_to_ulfstead_path_exists = railway.find_path('peel', 'ulfstead')
    harwick_to_peel_path_exists = railway.find_path('harwick', 'peel')
    harwick_to_godstone_path_exists = railway.find_path('harwick', 'godstone')

    print("A path exists between peel and ulfstead:")
    print(peel_to_ulfstead_path_exists)     # False
    print("A path exists between harwick and peel:")
    print(harwick_to_peel_path_exists)      # True
    print("A path exists between harwick and godstone:")
    print(harwick_to_godstone_path_exists)  # True
