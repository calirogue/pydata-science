# Objecs
# every object has:
# - a type
# - a internal data representation (a blueprint)
# - a set of procedures for interacting with the object (methods)
# an object is an instance of a particular type
# - you can find the type of an object by using: type()

# print(type(["A"]))
# <class 'list'>

# Methods
# - A class or type's methods are functions that every instance of that class
# or type provides
# - its how you interact with the data in an object
# - sorting is an example of a method that interacts with the data in the object

# Ratings = [10, 9, 5, 4, 2, 1]
# Ratings.sort()
# print(Ratings)

# Ratings.sort()
# Ratings.reverse()
# print(Ratings)


# --------- Class
# Data attributes

# Class Circle
# Data attributes: radius, color
# Class Rectangle
# Data attributes: color, height, width

# class Circle(object):

# class - class definition
# Circle - name of class
# (object): - class parent

# def __init__(self, radius, color)
# __init__ - special method or constructor used to initialize data attributes
# self - self parameter


# self.radius = radius
# self.color = color


# class Rectangle(object):
#     def __init__(self, color, height, width):
#         self.height = height
#         self.width = width
#         self.color = color

# >>>>
# ----------

# class Rectangle(object):
#     def __init__(self, 'blue', 10, 15):
#         self.height = 10
#         self.width = 15
#         self.color = 'blue'


# ---------- Methods

# class Circle(object):
#     def __init__(self, radius=2, color='blue'):
#         self.radius = 2
#         self.color = 'blue'

#     def add_radius(self, r):
#         self.radius = self.radius + r
#         # Methud used to add r to radius

#     def drawCircle(self):


# class Points(object):
#     def __init__(self, x, y):

#         self.x = x
#         self.y = y

#     def print_point(self):

#         print('x=', self.x, ' y=', self.y)


# p1 = Points("A", "B")
# p1.print_point()


# class Points(object):

#     def __init__(self, x, y):

#         self.x = x
#         self.y = y

#     def print_point(self):

#         print('x=', self.x, ' y=', self.y)


# p2 = Points(1, 2)

# p2.x = 'A'

# p2.print_point()
