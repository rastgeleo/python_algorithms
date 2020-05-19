def binary_search(values, target):
    """Binary search"""

    # set left and right
    left, right = 0, len(values) - 1
    while left <= right:
        # find the mid position of right and left and use it as a guess
        mid = (left + right) // 2
        if values[mid] == target:
            print('found at {}'.format(mid))
            return mid
        elif values[mid] > target:
            # guess was too high, adjust right as guess - 1
            right = mid - 1
            print('changing right', right)
        else:
            # guess was too low, adjust left as guess + 1
            left = mid + 1
            print('changing left', left)
    return None

def test_binary_search():
    target_list = list(range(10))
    assert binary_search(target_list, 5) == 5
    assert binary_search(target_list, 10) == None

if __name__ == "__main__":
    test_binary_search()
