import random

def bubble_sort(unordered):
    """
    Sorting through reapeted swap of adjacent elements
    run time of O(N^2)
    """
    size = len(unordered) - 1
    for i in range(size):
        for j in range(size-i):
            if unordered[j] > unordered[j+1]:
                tmp = unordered[j]
                unordered[j] = unordered[j+1]
                unordered[j+1] = tmp
                swap += 1
    return unordered


def test_bubble_sort():
    my_list = random.sample(range(-100, 100), 10)
    assert bubble_sort(my_list) == sorted(my_list)
    print('sorted :{}'.format(bubble_sort(my_list)))

if __name__ == "__main__":
    test_bubble_sort()
    bubble_sort([-93, -76, -47, -3, -1, 10, 24, 55, 66, 95])