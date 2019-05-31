# pie charts
# A pie chart is a circular statistical graphic divided into slices to
# illustrate numerical proportion.

# use panadas
# df_continents = df_canada.groupby('Continent', axis=0).sum()

# 1. import
import matplotlib.pyplot
import matplotlib as mpl

# 2. function
df_continents['Total'].plot(kind='pie')

plt.tital('immigrants to canada by continent')

# 3. show
plt.show()
