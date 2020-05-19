def is_palindrome(my_list):
    """O(N^2)"""
    while len(my_list) > 1:
        first = my_list[0]
        last = my_list[-1]
        if first != last:
            return False
        my_list = my_list[1:-1]
    return True


def is_palindrome_n(my_list):
    """O(N)"""
    last_index = len(my_list) - 1     # index of the last item
    for i in range(len(my_list)//2):  # Stop in the middle
        # compare letter with a letter at opposite index
        if my_list[i] != my_list[last_index-i]:
            return False
    return True


def is_palindrome_recursive(my_string):
    """recursive"""
    if len(my_string) == 0:
        return True
    if my_string[0] != my_string[-1]:
        return False
    return is_palindrome(my_string[1:-1])
