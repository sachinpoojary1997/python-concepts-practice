# a = b
# This creates a new reference to the same object.
# Both variables point to the same memory location.
# Any modification affects both.

# b = a.copy() (Shallow Copy)
# This creates a new outer list, but the inner objects are still shared.
# Modifying nested objects affects both, but replacing elements does not.

# copy.deepcopy(a)
# This creates a completely independent copy.
# Both outer and inner objects are duplicated.
# Changes in one will not affect the other.

import copy

# # Example of  copy 1
# a = [[1,2],3,4]
# b = a[:] # This creates a shallow copy of the list a b= a.copy() # This also creates a shallow copy of the list a
# a[1] = 10
# print("a:", a) # Output: a: [[1, 2], 10, 4]
# print("b:", b) # Output: b: [[1, 2], 3, 4]


# # Example of  copy 2
# a = [[1,2], [3,4]]
# b = a.copy()
# c = a

# a[0][0] = 99
# a[1] = [7,7]

# print("A:", a)
# print("B:", b)
# print("C:", c)

