import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("og array: ", arr)

print("addition: ", arr + 5)

print("subtraction: ", arr - 5)

print("multiplication: ", arr * 5)

print("division: ", arr / 2)

print("max: ", np.max(arr))
print("min: ", np.min(arr))

print("sorted: ", np.sort(arr))

print("reversed: ", arr[::-1])

print("array size: ", arr.size)

print("array shape: ", arr.shape)
