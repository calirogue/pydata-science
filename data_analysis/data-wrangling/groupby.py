# Grouping data
# Pandas dataframe, Groupby()
# - applied to categorical variables
# - group data into categories
# - single or multiple variables
# -

# Example:
df_test = df['barrel', 'charging-handle', 'bolt']
df_grp = df_test.groupby(
    ['barrel', 'charging-handle', 'bolt'], as_index=False).mean()


# pandas method - pivot()
# - one variable displayed along the columns and the other variable displayed
# along the rows.
#
df_pivot = df_grp.pivot(index='barrel', columns='charging-handle')

# heatmap
# - plot target variable over multi variables
# Example:
plt.pcolor(df_pivot, cmap='RdBBu')
plt.colorbar()
plt.show()
