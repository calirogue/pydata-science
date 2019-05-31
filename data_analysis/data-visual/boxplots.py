# box plots
# - A box plot is a way of statistically representing the distribution
# of given data through five main dimensions.


# 1. import
import matplotlib as mpl
import matplotlib.pyplot as plt

# 2. generate box plot
df_japan = df_canada.1oc[['japan'], years].transpose()

df_japan.plot(kind='box')

plt.title('box of japan immigrants')
plt.ylabel('# of immigrants')

# 3. show box plot
plt.show()
