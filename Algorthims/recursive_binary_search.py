def recursive_binary_search(list, target):
    """
    Returns True is target is within the list, else False
    """
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list) // 2)

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


# Numbers need to be sorted!
numbers = [x for x in range(1, 11)]

result = recursive_binary_search(numbers, 12)
print(result)

result = recursive_binary_search(numbers, 6)
print(result)
