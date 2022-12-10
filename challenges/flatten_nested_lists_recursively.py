""" Problem statement: We want to write a function that removes nested lists
    within a list but keeps the values contained.
    """


def flatten(nested_list: list):
    """
       Returns a flattened list from a list of nested arrays regardless of nested depth
    Args:
        nested_list (list): original list with elements at unknown depts of internal nesting

    Returns:
        flattened list of elements with no nesting
    """
    result = []

    if len(nested_list) == 0:
        return []

    if isinstance(nested_list[0], list):
        return flatten(nested_list[0]) + flatten(nested_list[1:])

    result.append(nested_list[0])
    return result + flatten(nested_list[1:])


# reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [
    [[[[[[[[[[[[[[[[[[[[[[[['jupiter', [[[[[[[[[[[[[[[[[[[['saturn']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], 'uranus', ['neptune', 'pluto']]


print(flatten(planets))
#output: ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
