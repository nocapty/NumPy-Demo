## Homework
import numpy as np
import matplotlib.pyplot as plt
1. #**Exercise 1**
t = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Array t:', t)

bruce_maxtrix = np.random.rand(4,4)
print('4*4 matrix', bruce_maxtrix)

bruce_maxtrix = np.arange(25)
print('orginal array', bruce_maxtrix)

reshaped = bruce_maxtrix.reshape(5, 5)
print('Reshaped array (5x5):', reshaped)

#**Exercise 2:**

def elements_product(arr1, arr2):
    return arr1 * arr2
    

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Array W:', arr1)

arr2 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
print('Array P:', arr2)

arr1 = np.array([[1, 2 , 3, 4,], [5, 6, 7, 8,]])
arr2 = np.array([5, 10, 15, 20])
print("Element-wise product (different shapes):", elements_product(arr1, arr2))

#**Challenge:**

samples = np.random.randn(1000)

plt.hist(samples, bins= 50, edgecolor='blue')
plt.title('Histogram of 1000 Random Samples from a Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()