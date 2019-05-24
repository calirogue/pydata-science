# data formating
# - data collected from different places in different formats


# data normalization
# - similar value range
# - similar intrinic influence on analyical model

# not normalized
# - "age" and "income" are different range
# - "income" will influence with result more

# Methods of normalizing data
# 1. simple feature scaling: xnew = xold / x max
df["length"] = df["length"]/df["length"].max()
# 2. Min-max: xnew = xold - xmin / xmax - x min
df["length"] = (df["length"]-df["length"].min()) /
(df["length"].max()-df["length"].min())
# 3. Z-score: xnew = xold - mu / sigma
df["length"] = (df["length"]-df["length"].mean()) / df["length"].std()
