def binary_search(target_list, start, end, target):
    if start > end:
        print('returning none')
        return None

    mid = (start + end) // 2

    if target_list[mid] == target:
        print('returning', mid)
        return mid

    if target_list[mid] < target:
        return binary_search(target_list, mid+1, end, target)
    else:
        return binary_search(target_list, start, mid-1, target)


def test_binary_search():
    target_list = list(range(10))
    size = len(target_list) - 1
    assert binary_search(target_list, 0, size ,5) == 5
    assert binary_search(target_list, 0, size, 10) == None

if __name__ == "__main__":
    test_binary_search()

