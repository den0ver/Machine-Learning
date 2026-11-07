import numpy as np

#1D array
arr1 = np.arange(1, 11)
print(f"One-Dimensional-Array\n{arr1}\n")

#2D array
arr2 = np.arange(1, 26).reshape(5, 5)
print(f"Two-Dimensional-Array\n{arr2}\n")

#3D array
arr3 = np.arange(1, 51).reshape(2, 5, 5)
print(f"Three-Dimensional-Array\n{arr3}\n")

#4D array
arr4 = np.arange(1, 81).reshape(2, 2, 5, 4)
print(f"Four-Dimensional-Array\n{arr4}")