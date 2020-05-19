from collections import deque

def bfs(graph, start, target):
    """BFS that returns the shortest path"""

    # initialise queue [start, [history of path]]
    q = deque([[start, [start]]])
    visited = [start]
    while q:
        # dequeue vertex and its path
        vertex, path = q.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                # found target - return path with itself
                if neighbor == target:
                    return path + [neighbor]
                # enqueue neighbors with path including neighbor vertex
                else:
                    q.append([neighbor, path+[neighbor]])
    return None

if __name__ == "__main__":
    

    some__graph = {
        'lava': set(['sharks', 'piranhas']),
        'sharks': set(['lava', 'bees', 'lasers']),
        'piranhas': set(['lava', 'crocodiles']),
        'bees': set(['sharks']),
        'lasers': set(['sharks', 'crocodiles']),
        'crocodiles': set(['piranhas', 'lasers'])
    }

    print(bfs(some__graph, 'crocodiles', 'bees'))