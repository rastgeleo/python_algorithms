def find_min(my_list):
    """recursive find_min fuction with O(NlogN)"""

    if not my_list:  # if my_list is empty, return None.
        return None
    if len(my_list) < 2:    # Base case. return element.
        return my_list[0]
    mid = len(my_list)//2
    first_half = my_list[:mid]
    last_half = my_list[mid:]
    min_1 = find_min(first_half)    # Divide the list into two
    min_2 = find_min(last_half)
    if min_1 < min_2:   # When reached base case, return smaller
        return min_1
    else:
        return min_2


def find_min_n(my_list, min=None):
    """recursive find_min function with O(N)"""

    if not my_list:
        return min
    if (min is None) or (my_list[0] < min):
        min = my_list[0]
    return find_min_n(my_list[1:], min)
