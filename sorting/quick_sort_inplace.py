import random

def quicksort(unsorted, start=0, end=None):
    """quicksort inplace"""
    if end is None:
        end = len(unsorted) - 1

    if start >= end:
        return

    # select random element to be pivot
    pivot_idx = random.randrange(start, end + 1)    # include idx end
    pivot_element = unsorted[pivot_idx]

    # swap random element with last element in sub-listay
    unsorted[end], unsorted[pivot_idx] = unsorted[pivot_idx], unsorted[end]

    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # we found an element out of place
        if unsorted[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            unsorted[i], unsorted[less_than_pointer] = unsorted[less_than_pointer], unsorted[i]
            # tally that we have one more lesser element
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements
    unsorted[end], unsorted[less_than_pointer] = unsorted[less_than_pointer], unsorted[end]

    # Call quicksort on the "left" and "right" sub-lists
    quicksort(unsorted, start, less_than_pointer-1)
    quicksort(unsorted, less_than_pointer+1, end)

    return unsorted

def test_quick_sort():
    my_list = random.sample(range(-100, 100), 10) 
    assert quicksort(my_list) == sorted(my_list)
    print('sorting: {}'.format(my_list))
    print('sorted :{}'.format(quicksort(my_list)))


if __name__ == "__main__":
    test_quick_sort()
