# histograms
# historgram is a way of representing the frequency distribution of a variable

# import
# import matplotlib as mpl
# import matplotlib.pyplot as plt

# df_canada['2013'].plot(kind='hist')

# plt.title('histogram of immgration in 2013')
# plt.ylabel('# of countries')
# plt.xlabel('# of immigrants')

# plt.show()

# with numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

count, bin_edges = np.histogram(df_canada['2013'])
df_canada['2013'].plot(kind='hist', xticks=bin_edges)

plt.title('histogram of immgration in 2013')
plt.ylabel('# of countries')
plt.xlabel('# of immigrants')

plt.show()
