def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in previous step

    Takes overall O(kn*logn) with python slicing
    Takes overall O(n*logn) without python slicing (using start and end vars)
    """
    if len(list) <= 1:  # Already sorted
        return list

    # Splits the list into sublists
    left_half, right_half = split(list)

    # Sort the sublists (recursively)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(k*logn)
    """
    midpoint = len(list) // 2

    left = list[:midpoint]  # Python slice operations take O(k) runtime
    right = list[midpoint:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Takes overall O(n)
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # When length of left list > length of right list
    while i < len(left):
        l.append(left[i])
        i += 1

    # When length of right list > length of left list
    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [55, 62, 93, 17, 31, 44, 77, 54, 20]
print(verify_sorted(alist))
print(verify_sorted(merge_sort(alist)))
