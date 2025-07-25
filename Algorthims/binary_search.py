def binary_search(list, target):
    """
    Search for a target value within a sorted list using binary search
    """
    first = 0
    last = len(list) - 1

    # Redefinig first/last reduces n by half -> O(log n)
    while (first <= last):
        midpoint = (first + last) // 2  # Rounds down to nearest whole number

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            # Redefine the first/last search area
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


# Numbers need to be sorted!
numbers = [x for x in range(1, 11)]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
