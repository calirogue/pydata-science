# # Two dimensional numpy

# a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
# # 'a' list above contains three different lists nested
# A = np.array(a)

# A.ndim: 2  # number of nested lists
# [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
# # first list is grouping the second list of the three thats nested

# A.shape: (3, 3)  # returns a tuple

# A.size: 9  # size gets the size of the array - which in this example is 9
# # 3 rows and 3 columns : 3 x 3 = 9

# # ------
# A = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
# [11, 12, 13]
# [21, 22, 23]
# [31, 32, 33]
# # A[1, 2] --- [1] goes to the second row, [2] goes to the third row
# # the value is 23

# # [1, 0, 1]
# # [2, 2, 2]
# # A[0, 1]
# # = 0


# # ---- Slicing:
# A[0, 2:2]
# [11, 12, 13]
# [21, 22, 23]
# [31, 32, 33]
# # answer would be the last two columns: 23, 33

# # ----- Arrays
# x = [1, 0][0, 1]
# y = [2, 1][1, 2]
# x + y = [[1+2][0+1][0+1][1+2]]
# # =
# [3, 1][1, 3]

# # add to an array
# X = np.array([[1, 0], [0, 1]])
# X = [1, 0], [0, 1]

# # add y
# y = np.array([[2, 1][1, 2]])
# y = [2, 1][1, 2]

# # result:
# Z = X = Y
# Z: array([[3, 1], [1, 3]])

# # multiply in an array
# Y = [2, 1][1, 2]
# 2Y = [2 x 2][2 x 1][2 x 1][2 x 2]
# # =
# [4, 2][2, 4]
# Z = 2 * Y
# Z: array([[4, 2], [2, 4]])

# X = [1, 0][0, 1]
# Y = [2, 1][1, 2]
# X * Y = [(1)2][(0)1][(0)1][(1)2]
# # =
# [2, 0][0, 2]

# X = np.array([[1, 0], [0, 1]])
# y = np.array([[2, 1][1, 2]])
# Z = X * Y
# Z: array([[2, 0], [0, 2]])

# # --------
# A = [0, 1, 1][1, 0, 1]
# [0, 1, 1]
# [1, 0, 1]

# B = [1, 1][1, 1][1, 1]
# [1, 1]
# [1, 1]
# [1, 1]

# A B = [0, 1, 1][1, 1, -1]
# 0 X 1 + 1 X 1 (-1) X 1 = 0
# [0, 1, 1]
# [1, 1, -1]
# # =
# A B =
# [0, 2]
# [0, 2]
