def counting_sort(unsorted):
    
    # construct counts list
    max_item = max(unsorted)
    counts = [0 for num in range(max_item+1)]   # 

    for item in unsorted:    # count the occurence of the number
        counts[item] += 1


    # shift counts to the right by one
    counts.insert(0, 0)
    counts.pop()


    # modify the counts so it inicates the start index of the item
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]


    # place the input list in sorted list according to the modified counts index
    sorted = [None for i in unsorted]
    for item in unsorted:
        idx = counts[item]
        sorted[idx] = item
        counts[item] += 1   # increment index by 1

    return sorted


print(counting_sort([1, 4, 1, 2, 7, 5, 2, 10, 4, 8]))


