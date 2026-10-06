# Python list as array
arr = [10, 20, 30, 40, 50]

# O(1) access
print("First element:", arr[0])
print("Last element:", arr[-1])

# O(n) traversal
for x in arr:
 print(x)

# O(n) insertion (worst case)
arr.insert(0, 5)
print("After insertion:", arr)

# O(n) deletion
arr.remove(30)
print("After deletion:", arr)