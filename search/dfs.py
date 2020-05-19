def dfs(graph, current, target, visited=None):
    """DFS with recursion"""

    # initialise visited list if none
    if visited is None:
        visited = []

    visited.append(current)

    # base case: the path exist. return visited list
    if  current == target:
        print('found ', current)
        return visited

    for neighbor in graph[current]:
        if neighbor not in visited:
            print('visiting:', neighbor)
            path = dfs(graph, neighbor, target, visited)
            # if path returned, hit the base case and found the path
            # else it will return None
            if path:
                return path

if __name__ == "__main__":
    

    some__graph = {
        'lava': set(['sharks', 'piranhas']),
        'sharks': set(['lava', 'bees', 'lasers']),
        'piranhas': set(['lava', 'crocodiles']),
        'bees': set(['sharks']),
        'lasers': set(['sharks', 'crocodiles']),
        'crocodiles': set(['piranhas', 'lasers'])
    }

    print(dfs(some__graph, 'crocodiles', 'bees'))