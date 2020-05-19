import random
def insert_sort(unsorted):
    
    print('start sorting: {}'.format(unsorted))
    for i in range(1, len(unsorted)):

        pointer = i
        value = unsorted[pointer]

        while pointer > 0 and unsorted[pointer-1] > value:
            unsorted[pointer] = unsorted[pointer-1]

            pointer -= 1
        
        unsorted[pointer] = value
        print('sorting: {}'.format(unsorted))
    
    print('sorted: {}'.format(unsorted))
    return unsorted

def test_insert_sort():
    unsorted = random.sample(range(20), 20)
    assert insert_sort(unsorted) == sorted(unsorted)

if __name__ == "__main__":
    test_insert_sort()