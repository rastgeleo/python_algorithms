from math import inf, sqrt
from heapq import heappop, heappush
from euclidean_graph import euclidean_graph, bengaluru, jaipur
from manhattan_graph import manhattan_graph, cuny_grad_center, grand_central_station, simple_graph, a, e

def heuristic(start, target):
    """euclidian heuristic """
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return sqrt(x_distance**2 + y_distance**2)

def heuristic_manhattan(start, target):
    """manhattan heuristic with no diagnal movement"""
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance


def a_star(graph, start, target, hf):
    print("Starting A* algorithm!")
    count = 0
    
    paths_and_distances = {}    # dictionary tracing f(x) = g(x) + h(x) :estimated distance

    g_distance = {}             # dictionary of g(x) :sum of distances from the origin
    
    for vertex in graph:
        # traking a route as a list
        g_distance[vertex] = inf
        paths_and_distances[vertex] = [inf, [start.name]]

    paths_and_distances[start][0] = 0
    g_distance[start] = 0

    vertices_to_explore = [(0, start)]
    while vertices_to_explore and paths_and_distances[target][0] == inf:
        _ , current_vertex = heappop(vertices_to_explore)
        #print('visiting {}'.format(current_vertex.name))
        for neighbor, edge_weight in graph[current_vertex]:
            # added heuristic function value
            new_distance = (g_distance[current_vertex] +
                edge_weight + hf(neighbor, target))
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]

            if new_distance < paths_and_distances[neighbor][0]:
                #print('since {} is less than {}'.format(new_distance, paths_and_distances[neighbor][0]))
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                g_distance[neighbor] = g_distance[current_vertex] + edge_weight
                heappush(vertices_to_explore, (new_distance, neighbor))
                #print('new distance of {} is {}'.format(neighbor.name, new_distance))
                count += 1
                #print("\nAt " + vertices_to_explore[0][1].name)

    print("Found a path from {0} to {1} in {2} steps: ".format(
        start.name, target.name, count), paths_and_distances[target][1])

    return paths_and_distances[target][1]

# Call a_star() on euclidean_graph to find the best route
# from jaipur to bengaluru:
a_star(manhattan_graph, cuny_grad_center, grand_central_station, heuristic_manhattan)
#a_star(simple_graph, a, e)