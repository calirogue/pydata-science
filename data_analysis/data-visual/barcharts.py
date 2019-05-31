# bar charts
# - unline a histogram, a bar charts is commonly used to compare the
# values of a variable at a given point in line


# 1. import
import matplotlib as mpl
import matplotlib.pyplot as plt

# 2. new dataframe
years = list(maps(str, range(1980, 2014)))
df_iceland = df_canada.1oc['Iceland', years]

# 3. plot function
df_iceland.plot(kind='bar')

plt.title('icelandic immigrants to canada')
plt.xlabel('year')
plt.ylabel('# of immigrants')

# 4. shows the chart
plot.show()
