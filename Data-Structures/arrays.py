new_list = [1, 2, 3]  # Initialize a new list and
                      # Allocates a base amount of memory
                      # Arrays store references to the objects
                      # in memory (accessed by index).
                      # Arrays have a reference to the base address
                      # of the memory block allocated for the array.

# Access an element
result = new_list[0]  # O(1)

# Searching for an element using linear search
if 1 in new_list: print("True") # O(n)

for n in new_list:
    if n == 1:
        print(True)
        break
