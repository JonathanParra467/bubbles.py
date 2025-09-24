"""
Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.
"""
names = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

n = len(names)
for i in range(n):
    for j in range(0, n - i - 1):
        if names[j] > names[j + 1]:
            names[j], names[j + 1] = names[j + 1], names[j]

print("Sorted list: ", names)

names.reverse()

print("Reversed list: ", names)