def sparse_search(data, search_val):
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))
    first = 0
    last = len(data) - 1

    while first <= last:
        mid = (first+last) // 2
        print(mid)

        # if data is empty, find nearest data which is not empty
        if not data[mid]:
            left = mid - 1
            right = mid + 1
            while True:
                if left < first and right > last:
                    # Whole data is empty
                    print('{} is not in the dataset'.format(search_val))
                    return
                if right <= last and data[right]:
                    # found one which is not empty set it to the mid index
                    mid = right
                    break
                if left >= first and data[left]:
                    mid = left
                    break
                left = left - 1
                right = right + 1

        # Below codes are the usual binary search
        if data[mid] == search_val:
            print('{} found at position {}'.format(search_val, mid))
            return
        elif search_val < data[mid]:
            last = mid - 1
        else:
            first = mid + 1
    print('{} is not in the dataset'.format(search_val))

if __name__ == "__main__":
    
    sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "C")
    sparse_search(["A", "B", "", "", "E"], "A")
    sparse_search(["", "X", "", "Y", "Z"], "Z")
    sparse_search(["A", "", "", "", "B", "", "", "", "C"], "D")
    sparse_search(["Apple", "", "Banana", "", "", "", "", "Cow"], "Banana")
    sparse_search(["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"], "Parth")
