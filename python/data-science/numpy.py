# one dimensional numpy


# numby array:
# # a = ["0", 1, "two", "3", 4]
# a[0]:"0"
# a[1]:1
# a[2]:"two"
# a[3]:"3"
# a[4]:4

# similar to a list

# import numpy as np

# a = np.array([0, 1, 2, 3, 4])

# basic operations
# - Vector addition and substraction
#
# normal python:
# z = u + v
# u = [1, 0]
# v = [1, 0]
# z = []

# for n, m in zip(u, v):
#     z.append(n+m)

#
# numpy:
# u = np.array([1, 0])
# v = np.array([0, 1])
# z = u + v
# z: array([1, 1])

# subtraction
#
# numpy:
# u = np.array([1, 0])
# v = np.array([0, 1])
# z = u - v
# z: array([1, -1])

# normal python:
# u = [1, 0]
# v = [1, 0]
# z = []

# for n, m in zip(u, v):
#     z.append(n-m)


# -----
# array multiplication with a scalar

# numpy
# y = np.array([1, 2])
# z = 2*y
# z: array([1, 4])


# -----
# Product of two numpy arrays
# z = u * v

# u = np.array([1, 2])
# v = np.array([3, 2])

# z = u * v

# z: array([3, 4])

# Dot product
# u = np.array([1, 2])
# v = np.array([3, 2])

# result = np.dot(u, v)

# result: 5


# Adding Constant to an numpy array
# u = np.array([1, 2, 3, -4])

# Universal functions
# apply universal functions to numpy array
#
#  Find the average:
# a = np.array([1, -1, 1, -1])
# mean_a = a.mean()
# mean_a: 0, 0

# #  result is 0

#
#  Find the max:
# b = np.array([1, -2, 3, 4, 5])
# max_b = b.max()
# max_b: 5

# # result is 5

# access pi:
# np.pi

# line space:
# np.linspace(-2, 2, num=5)w
# returns evenly spaced mumbers by interval


# plotting mathematical functions
# x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x)

# will help plot the function
# import matplotlib.pyplot as plt

# for jupyter notebook:
# use: %matplotlib inline
# to display the plot
# plt.plot(x, y)
# x is for the horizontal
# y is for the vertical
