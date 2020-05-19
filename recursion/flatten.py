def flatten(my_list):
    result = []
    for element in my_list:
        if isinstance(element, list):
            flat_list = flatten(element)
        # extend the returned value and make it one list.
        result.extend(flat_list)
    else:
        # Base case. just append item to the result.
        result.append(element)
    return result


### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

result = flatten(planets)
print(result)