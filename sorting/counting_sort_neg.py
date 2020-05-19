import random

def counting_sort(unsorted):
    """ counting sort that takes negative values as input"""
    
    # construct counts list
    max_item = max(unsorted)
    min_item = min(unsorted)
    # the list starts from the minimum value with index 0
    # So we need to correct the index when we refer later. idx + abs(min_item)
    # e.g if the range of input is [-3, 3], the value 0 counts goes into 0+3 = 4.
    abs_min = abs(min_item)
    counts = [0 for num in range(min_item, max_item+1)] 

    for item in unsorted:    # count the occurence of the number
        counts[item+abs_min] += 1

    # shift counts to the right by one
    counts.insert(0, 0)
    counts.pop()

    # modify the counts so it inicates the start index of the item
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    # place the input list in sorted list according to the modified counts index
    sorted = [None for i in unsorted]
    for item in unsorted:
        idx = counts[item+abs_min]
        sorted[idx] = item
        counts[item+abs_min] += 1   # increment index by 1

    return sorted


def test_counting_sort():
    my_list = random.sample(range(-100, 100), 10)
    assert counting_sort(my_list) == sorted(my_list)
    print('sorting: {}'.format(my_list))
    print('sorted :{}'.format(counting_sort(my_list)))

if __name__ == "__main__":
    test_counting_sort()