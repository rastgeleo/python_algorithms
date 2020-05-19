def depth(tree):
    """Count levels of a tree structure using loop"""
    result = 0
    # our "queue" will store nodes at each level
    queue = [tree]
    # loop as long as there are nodes to explore
    while queue:
        # count the number of child nodes
        level_count = len(queue)
        for child_count in range(0, level_count):
            # loop through each child
            child = queue.pop(0)
           # add its children if they exist
            if child.get("left_child", None):
                queue.append(child["left_child"])
            if child.get("right_child", None):
                queue.append(child["right_child"])
        # count the level
        result += 1
    return result


def depth_recursive(tree):
    """Count levels of a tree structure using recursive"""
    if not tree:
        return 0
    left_depth = depth(tree.get("left_child", None))
    right_depth = depth(tree.get("right_child", None))

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


two_level_tree = {
    "data": 6,
    "left_child":
    {"data": 2}
}

four_level_tree = {
    "data": 54,
    "right_child":
    {"data": 93,
     "left_child":
     {"data": 63,
      "left_child":
      {"data": 59}
      }
     }
}

def test_depth():
    print(depth(two_level_tree) == 2)
    print(depth(four_level_tree) == 4)

test_depth()
