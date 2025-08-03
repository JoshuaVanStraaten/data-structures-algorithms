def sum(numbers):
    if not numbers:
        return 0
    print(f"Calling sum({numbers})")
    remaining_sum = sum(numbers[1:])
    print(f"Call to sum({numbers}) returning {numbers[0]} + {remaining_sum}")
    return numbers[0] + remaining_sum


print(sum([1, 2, 7, 9]))
