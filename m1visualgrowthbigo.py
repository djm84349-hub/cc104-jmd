import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)
o1 = np.ones_like(n)
on = n
on2 = n**2
ologn = np.log2(n)

plt.plot(n, o1, label="O(1)")
plt.plot(n, on, label="O(n)")
plt.plot(n, on2, label="O(n^2)")
plt.plot(n, ologn, label="O(log n)")
plt.legend()
plt.xlabel("Input size (n)")
plt.ylabel("Operations")
plt.title("Big-O Growth Rates")
plt.show()