import random

def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result.extend(left)

    if right:
        result.extend(right)

    return result

def test_merge_sort():
    my_list = random.sample(range(-100, 100), 10)
    assert merge_sort(my_list) == sorted(my_list)
    print('sorted :{}'.format(merge_sort(my_list)))


if __name__ == "__main__":
    test_merge_sort()