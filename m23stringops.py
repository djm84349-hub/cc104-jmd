s = "hello world"

# O(1) access
print("First char:", s[0])

# O(n) traversal
for c in s:
 print(c, end=" ")

# O(n) concatenation (new string created each time)
s2 = s + "!!!"
print("\nConcatenated:", s2)

# O(n) substring search
print("Contains 'world'?", "world" in s)