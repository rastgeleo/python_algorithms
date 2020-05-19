import heapq

graph = {
        'start': {'a': 6, 'b': 2},
        'a': {'fin': 1},
        'b': {'a': 3, 'fin':5},
        'fin': {}
         }


def dijkstra(graph, origin):

    inf = float('inf')

    # setup table for distance and previous vertice.
    dist = {}
    prev = {}
    
    # create heapq to use.
    q = []

    dist[origin] = 0
    for v in graph.keys():
        if v != origin:
            dist[v] = inf
            prev[v] = None
        heapq.heappush(q, (dist[v], v))
    

    visited = []
    while q:
        distance, current = heapq.heappop(q)
        if current in visited:
            #skip already visited vertice.
            continue
        print('visiting : {} distance from the origin : {}'.format(current, distance))
        neighbors = graph[current]
        # loop through current vertice's neighbors.
        for n in neighbors.keys():
            new_distance = dist[current] + graph[current][n]
            if new_distance < dist[n]:  
                # if distance to n via current is shorter, update the table.
                dist[n] = new_distance
                prev[n] = current
                heapq.heappush(q, (new_distance, n))
                print('updating {} with new distance : {}'.format(n, new_distance))
        print(q)
        visited.append(current)
    
    return dist, prev
    

if __name__ == "__main__":
    dist, prev = dijkstra(graph, 'start')
    print(dist)