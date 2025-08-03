numbers = [5, 8, 1, 4, 7]


def merge_sort(values):
    # Base case
    if len(values) <= 1:
        return values

    # Recursive case
    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    print(f"Left: {left_values}, Right: {right_values}")
    sorted_values = []
    left_index = 0
    right_index = 0
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] <= right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    # Append any remaining elements
    sorted_values.extend(left_values[left_index:])
    sorted_values.extend(right_values[right_index:])
    return sorted_values


print(numbers)
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
