def merge_sort(numbers):
    """
    merge sort
    """
    # base case
    if len(numbers) == 1:
        print('hit the base', numbers)
        return numbers

    print('splitting', numbers)
    mid = len(numbers)//2
    left = numbers[:mid]
    right = numbers[mid:]

    # recursive call
    left = merge_sort(left)
    right = merge_sort(right)

    # construct result list.
    result = []
    while len(left) > 0 or len(right) > 0:
        print('comparing', left, right)
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    print('merging', result)
    return result
