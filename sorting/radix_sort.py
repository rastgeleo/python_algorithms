# problem: It doens't sort if negative numbers are in the list.

def radix_sort(to_be_sorted):
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))
    being_sorted = to_be_sorted[:]

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position

        digits = [[] for i in range(10)]   # make 10 buckets

        for number in being_sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
                digit = int(digit)
                digits[digit].append(number)
            except IndexError:              # if index error, put it in 0 bucket
                digit = 0
            digits[digit].append(number)
        print('i')
        # flatten the list
        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)
    print(being_sorted)
    return being_sorted


