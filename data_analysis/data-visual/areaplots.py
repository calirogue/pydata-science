# Area plot
# - Also known as area chart or area graph
# - commonly used to represent cumulated totals using
# numbers or percentages over time
# - based on the line plot


# generating area plots
# df_x.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# create a new data frame
# years = list(map(str, range(1980, 2014)))

# df_x.sort_values(['Total'], ascending=False, axis=0, inplace=True)
# df_top5 = df_x.head()
# df_top5 = df_top5[years].transpose()


# 1. import
import matplotlib as mpl
import matpotlib.pyplot as plt

df_top5.plot(kind='area')

plt.title('immigration trend of top 5 countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()
