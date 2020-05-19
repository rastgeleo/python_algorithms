def merge_sort(A):
    # base case
    if len(A) > 1:
        print('splitting', A)
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)

        # initialises pointers for left (i) right (j) and output array (k)
        i = j = k = 0

        # compare left list to right list. add the smaller one to the result
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i = i + 1
            else:
                A[k] = right[j]
                j = j + 1
            k = k + 1

        # if only left or right array left, deal with it.
        while i < len(left):
            A[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            A[k] = right[j]
            j = j + 1
            k = k + 1

    print('merging', A)
    return(A)
