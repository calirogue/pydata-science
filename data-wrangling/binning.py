# binning:
# 1. grouping of values into "bins"
# 2. converts numeric into categorical variables
# 3. group a set of numerical values into a set of "bins"

# numpy:
# 1.
bins = np.linspace(min(df["price"]), max(df["price"]), 4)
# 2.
group_names = ["low", "medium", "high"]
# 3.
df["price-binned"] = pd.cut(df["price"], bins,
                            labels=group_names, include_lowest=True)
