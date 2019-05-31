# scatter plots
# - A scatter plot is a type of plot that displays values pertaining to typically
#  two variables against each other.
# - Usually it is a dependent variable to be plotted against an independent
# variable in order to determine if any correlation between the two variables
# exists.

# 1. import
import matplotlib as mpl
import matplotlib.pyplot as plt

# 2. generate scatter plot function
df_total.plot(
    kind='scatter',
    x='year',
    y='total',
)

plt.title('total immigrant population')
plt.xlabel('year')
plt.ylabel('# of immigrants')

# 3. show
plt.show()
