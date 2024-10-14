from icecream import ic
def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        # the s returns what was popped
        s = queue.pop(0)
        print(s, end=" ") # ends the output with a space
        
        for node in graph[s]:
            # ic(node)
            ic(visited)
            ic(queue)
            if node not in visited:
                visited.append(node)
                queue.append(node)
        
                
        # break
    # ic(s)
    return s


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E", "F"],
        "C": ["G"],
        "D": [],
        "E": [],
        "F": ["H"],
        "G": ["I"],
        "H": [],
        "I": []
    }

    bfs(graph, "A")