# Basic plotting with matplotlib

# - use jupyter notebook
# import:
# import matplotlib as apl
# print('matplotlib version: ', apl.__version__)

# plot function
import matplotlib.pyplot as plt
plt.plot(5, 5, 'o')
plt.show()

# show in a different browser:
# %matplotlib inline

# pandas has a built-in notation of it
# - using matplotlib with pandas.
# Example:
india_china_df.plot(kind="line")
# histogram
india_china_df["india"].plot(kind="hist")
