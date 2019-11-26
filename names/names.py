import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

"""Runtime complexity of above is O(len(names_1) * len(names_2))"""

tree = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    tree.insert(name)
duplicates = []
for name in names_2:
    if tree.contains(name):
        duplicates.append(name)

"""Now runtime complexity is O(n log n)"""

# duplicates = []
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

"""If constrained to using lists, I might do something like the above.
Now runtime complexity is O(len(names_1)). We have two O(n) operations;
looping thru names_1, and a lookup in names_2."""

# duplicates = set(names_1) & set(names_2)

"""This is obviously super fast and what I'd really do.
Now runtime complexity is O(min(len(names_1), len(names_2))). However, this time we
perform only one such operation."""

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
