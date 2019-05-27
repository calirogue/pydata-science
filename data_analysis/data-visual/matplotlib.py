# -- Matplotlib arachitecture - -
# - Scripting layer
# - Artist Layer(artist)
# - Backend layer(FigureCanvas, Renderer, Event)

# Backend layer
# - has three built-in abstract interface classes:
# 1. FigureCanvas:
# matplotlib.backend_bases.FigureCanvas
# - Encompasses the area onto which the figure is drawn

# 2. Renderer:
# matplotlib.backend_bases.Renderer
# - Knows how to draw on the FigureCanvas

# 3. Even:
# matplotlib.backend_bases.Event
# - Handles user inputs such as keyboard strokes and mouse clicks


# Artist layer
# - comprised of one main object - Artist:
#     - Knows how to use the Renderer to draw on the canvas.
# - Title, lines, tick labels, and images, all correspond to individual artist
# instances
# - two types of artist objects
# 1. Primitive: Line2D, Retangle, Circle, and Text
# 2. Composite: Axis, tick, axes, and figure
# - Each composite artist may contain other composite artist
# as well as primitive artists

# Example:

# import Figurecanvas
# import numpy as np
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# # import Figure artist
# from matplotlib.figure import Figure
# fig = Figure()
# canvas = FigureCanvas(fig)

# # create 10000 random numbers using numpy
# x = np.random.randn(10000)

# # create an axes artist
# ax = fig.add_subplot(111)

# # generate a histogram of the 10000 numbers
# ax.hist(x, 100)

# # add a title to the figure and save it
# ax.set_title('Normal distribution with $\mu=0, \sigma=$')
# fig.savefig('matplotlib_histogram.png')

# Scripting layer
# - comprised mainly of pyplot, a scripting interface that is lighter than the
# artist layer
#  - how to generate the same histogram of 10000 random values using pyplot interfact
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, 100)
plt.title(r'Normal distribution with $\mu=0, \sigma=$')
plt.savefig('matplotlib_histogram.png')
plt.show
