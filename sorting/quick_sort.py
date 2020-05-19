import random

def quick_sort(items):
    if len(items) <= 1:
        return items

    pivot = items[0]
    lt = quick_sort([item for item in items[1:] if item < pivot])
    gte = quick_sort([item for item in items[1:] if item >= pivot])
    return lt + [pivot] + gte
    

def test_quick_sort():
    my_list = random.sample(range(-100, 100), 10)
    assert quick_sort(my_list) == sorted(my_list)
    print('sorting: {}'.format(my_list))
    print('sorted :{}'.format(quick_sort(my_list)))

if __name__ == "__main__":
    test_quick_sort()