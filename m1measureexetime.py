import time

n = 10_000_000

start = time.time()
sum_iterative = (n)
end = time.time()
print("Iterative:", end - start, "seconds")

start = time.time()
sum_formula = (n)
end = time.time()
print("Formula:", end - start, "seconds")